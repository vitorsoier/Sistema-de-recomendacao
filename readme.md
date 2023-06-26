# Sistema de recomendação

## Introdução

Esse projeto tem como o objetivo me fazer aprofundar e praticar conceitos de ML.
Para esse projeto faremos um sistema de recomendação. Existem basicamente três tipos de sistemas de recomendação:

* Content-based filtering
* Collaborative filtering
* Hybrid

Content-based filtering o que significa que nosso sistema de recomendação vai levar em conta itens que o usuario tenha gostado anteriormente para fazer a indicação de novos itens para consumo. Esse modelo tem como problema principal o fato que não conseguimos indicar coisas muito diferentes que o nosso cliente pode gostar. Exemplificando, se um usuario consume apenas musicas no estilo samba, vamos indicar musicas com um estilo muito proximo o que pode ser ruim caso nosso usuario queria experimentar um novo estilo musical.

# Dados

Para esse projeto usaremos os dados disponibilizados pelo IMDB no seu site, vamos coletar esses dados diretamente da API aberta do site. Conseguimos coletar 10.000 filmes que farão parte do nosso projeto. Para obter acesso a API do IMDB basta acessar o [site](https://developer.themoviedb.org/reference/intro/getting-started) e criar um usuario e obter sua chave para fazer requisições a API.
