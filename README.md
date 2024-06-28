```markdown
# Movie Recommendation System

This project is a simple movie recommendation system built with Flask and a movie dataset. It allows users to input their favorite movie and get recommendations for similar movies based on a content-based filtering approach.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/imisgsc/MOVIE-RECOMMENDATION-SYSTEM.git
   cd MOVIE-RECOMMENDATION-SYSTEM
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the dataset file `movies.csv` in the `data` directory.

## Usage

1. Run the Flask app:

   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Enter the name of your favorite movie and click the "Get Recommendations" button to see a list of recommended movies.

## Project Structure

```
MOVIE-RECOMMENDATION-SYSTEM/
├── app.py                     # Main Flask application
├── data/
│   └── movies.csv             # Dataset file
├── models/
│   └── recommendations_model.py # Recommendation model script
├── static/
│   ├── css/
│   │   └── styles.css         # CSS styles
├── templates/
│   └── index.html             # Main HTML template
├── requirements.txt           # Required Python packages
└── README.md                  # Project README file
```
