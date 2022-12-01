import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5cf45311a8f5352f5cb1f86a4f3a692f&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommended(movie):
    movieindex = movies[movies['original_title'] == movie].index[0]
    distances = similarity[movieindex]
    movieslist = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movies = []
    recommended_movies_poster  = []
    for i in movieslist:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].original_title)
        # get poster
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie recommender system')

opted_movie = st.selectbox('Enter movie you want to search',movies['original_title'].values)
if st.button('Recommend'):
    names,posters = recommended(opted_movie)

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