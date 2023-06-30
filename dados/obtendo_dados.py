import os
import requests
import json
import pandas as pd

key = os.getenv("apiKey")
headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {key}"
        }

def extract_filmes(headers, pages = 500):
    """ Seleciona a lista de filmes do tmdb
    ARGS:
        headers(dict) : Dicionario com detalhes da requisição
        pages(int): Limite de paginas retornadas da api
    """
    responses_filmes = []
    for page in range(1, pages+1):
        url_filmes = f"https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={page}"
    
        
        response_filmes = requests.get(url_filmes, headers=headers)
        responses_filmes.extend(response_filmes.json()['results'])

    return responses_filmes

def extract_genero(headers):
    """ Seleciona a lista de generos do tmdb
    ARGS:
        headers(dict) : Dicionario com detalhes da requisição
    """
    url_genero = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    response_genero = requests.get(url_genero, headers=headers)
    
    return response_genero

def transform(raw_data, tipo):
    """ Transforma os dados retirados da API em dados um df
    ARGS:
        raw_data(dict) : Retorno de uma API
        tipo(string): filmes ou genero
    """
    if tipo == 'filmes':
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
    
    if tipo == 'genero':
        data = raw_data.json()['genres']
        df = pd.DataFrame(data)
        
        if df.isnull().values.any():
            raise Exception("Valor nulo")
    
    return df

def para_csv(df, caminho):
    """ Transforma o df em dados um arquivo csv
    ARGS:
        df(DataFrame) : DataFrame com qualquer dado
        caminho(string): pasta e nome do arquivo que vai ser salvo
    """
    df.to_csv(caminho, index=False)

raw_data_filmes = extract_filmes(headers = headers, pages=500, )
raw_data_genero = extract_genero(headers = headers)
df_filmes = transform(raw_data_filmes, 'filmes')
df_genero = transform(raw_data_genero, 'genero')
para_csv(df_filmes, 'dados/filmes.csv')
para_csv(df_genero, 'dados/generos.csv')




