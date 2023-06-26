import os
import requests
import json
import pandas as pd

key = os.getenv("apiKey")

def extract_filmes(pages = 500):
    """ Seleciona a lista de filmes do tmdb
    ARGS:
        pages(int): Limite de paginas retornadas da api
    """
    responses = []
    for page in range(1, pages+1):
        url = f"https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={page}"
    
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {key}"
        }
    
        response = requests.get(url, headers=headers)
        responses.extend(response.json()['results'])

    return responses

def transform(raw_data):
    filmes = []
    for info in raw_data:
        filmes.append(
            {
                'id': info['id'],
                'id_genero': info['genre_ids'],
                'titulo': info['title'],
                'resumo': info['overview'],
                'lancamento': info['release_date'],
                'idioma_original': info['original_language']
            }
        )
    df = pd.DataFrame(filmes)

    # validation
    if not df["id"].is_unique:
        raise Exception("Valor de id não é unico")
    if df.isnull().values.any():
        raise Exception("Valor nulo")
    
    return df

raw_data = extract_filmes(pages=500)
df = transform(raw_data)
df.to_csv('filmes.csv', index=False)



