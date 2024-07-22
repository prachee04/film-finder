# Movie Recommender System
Welcome to the Movie Recommender System! This web application recommends similar movies based on content using Bag of Words Vectorization. The system analyzes movie metadata to provide users with suggestions for movies they might enjoy.

## Live Demo

Check out the live demo of the web application here: [Film Finder](https://film-finder.streamlit.app/)

## Dataset

The dataset used for this project is sourced from Kaggle.

## Features

- **Movie Selection**: Users can select a movie from a dropdown list.
- **Recommendation System**: The app recommends similar movies based on the selected movie.
- **Display Recommendations**: The app shows the recommended movie titles along with their posters.

## How It Works

1. **Data Loading**: The app loads movie metadata and the similarity matrix from the pickle files.
2. **Movie Selection**: Users select a movie from the dropdown menu.
3. **Recommendation**: Upon clicking the "Show Recommendation" button, the app computes the top 5 similar movies using the similarity matrix.
4. **Display**: The app displays the recommended movies along with their posters in a visually appealing layout.
