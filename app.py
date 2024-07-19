import streamlit as st
import pickle 
import pandas as pd
from helper import  recommend_tfidf
import requests
# API - c74d8b0ca4a5f0e2078d0f7dd891cbd5

movies_dict = pickle.load(open("movies_dict.pkl", 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", 'rb'))

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=c74d8b0ca4a5f0e2078d0f7dd891cbd5&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend_tfidf(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_moives_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)

        #fetch poster from API
        recommended_moives_posters.append(fetch_poster(movie_id))
    
    return recommended_movies, recommended_moives_posters

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Select a Movie',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend_tfidf(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    
    with col4:
        st.text(names[3])
        st.image(posters[3])
    
    with col5:
        st.text(names[4])
        st.image(posters[4])