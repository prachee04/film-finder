import streamlit as st
import pickle
import pandas as pd


st.title("Film Finder: Movie Recommender")
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
#select box
option = st.selectbox("Select your movie", (movies))

