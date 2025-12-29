import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key="YOUR_API_KEY""
    response = requests.get(url)
    data = response.json()

    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path
    else:
        return None


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommend_movies = []
    recommend_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
         # fetch poster from api
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies, recommend_movies_poster

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select your favourite kind of movie', movies['title'].values)

if st.button('Recommend'):
    name, poster = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        if poster[0]:
            st.image(poster[0])

    with col2:
        st.text(name[1])
        if poster[1]:
            st.image(poster[1])

    with col3:
        st.text(name[2])
        if poster[2]:
            st.image(poster[2])

    with col4:
        st.text(name[3])
        if poster[3]:
            st.image(poster[3])

    with col5:
        st.text(name[4])
        if poster[4]:
            st.image(poster[4])
