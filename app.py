from flask import Flask, render_template, request
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load data and set up recommendation logic
movies_data = pd.read_csv('data/movies.csv')  # Adjust path as necessary

# Selecting the relevant features for recommendation
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

# Replacing missing values with empty strings
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# Combining all selected features
combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']

# Converting text data to feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Getting similarity scores using cosine similarity
similarity = cosine_similarity(feature_vectors)

# Recommendation function
def recommend_movies(movie_name):
    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    
    if find_close_match:
        close_match = find_close_match[0]
        index_of_the_movie = movies_data[movies_data.title == close_match].index[0]
        
        similarity_scores = list(enumerate(similarity[index_of_the_movie]))
        sorted_similar_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        
        recommendations = []
        for i, movie in enumerate(sorted_similar_movies):
            index = movie[0]
            title_from_index = movies_data.loc[index, 'title']
            recommendations.append(title_from_index)
            if i >= 4:  # Adjust the number of recommendations shown
                break
        return recommendations
    else:
        return []

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    movie_name = request.form['movie_name']
    if movie_name:
        recommendations = recommend_movies(movie_name)
    else:
        recommendations = []
    return render_template('recommendations.html', movie_name=movie_name, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
