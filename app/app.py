import os
import pandas as pd
import pickle
import requests
import streamlit as st
import streamlit.components.v1 as components


with open('app/df_filmes_process.pkl', 'rb') as arquivo:
    movies = pickle.load(arquivo)

with open('app/similarity.pkl', 'rb') as arquivo:
    similarity = pickle.load(arquivo)


def get_poster(movie_id, df = pd.read_csv('dados/filmes.csv')):
     filter = df.query(f'id == {movie_id}')
     poster_path = filter.iloc[0].poster
     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
     return full_path

def recomendation_system(movie):
    id_of_movie = movies[movies['titulo']==movie].index[0]
    distances = similarity[id_of_movie]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    recommend_movies = []
    recommend_poster = []
    for movie_id in movie_list:
        id = movies.iloc[movie_id[0]].id
        recommend_movies.append(movies.iloc[movie_id[0]].titulo)
        recommend_poster.append(get_poster(id))
    return recommend_movies, recommend_poster

st.set_page_config(page_icon="🎥", page_title="Sistema de recomedação")
st.set_page_config(layout="wide")

movies_ordenados = movies.sort_values(by='titulo')

st.header("Sistema de Recomendação de filmes")

select_value = st.selectbox("Selecione um filme", movies_ordenados['titulo'])


if st.button("Mostrar recomendações"):
    rec_movies, movie_poster = recomendation_system(select_value)
    columns = [col1, col2, col3, col4, col5] = st.columns(5)
    count = 0
    for col in columns:
        with col:
            st.text(rec_movies[count])
            st.image(movie_poster[count])
        count += 1

