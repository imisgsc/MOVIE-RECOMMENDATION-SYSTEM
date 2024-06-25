# app.py

from flask import Flask, render_template, request
from models.recommendation_model import recommend_movies

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    title = request.form['title']
    recommendations = recommend_movies(title)
    return render_template('recommendations.html', title=title, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
