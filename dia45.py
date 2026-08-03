import requests
from bs4 import BeautifulSoup
import os


# Página arquivada com a lista dos filmes
ENDERECO_SITE = (
    "https://web.archive.org/web/20200518073855/"
    "https://www.empireonline.com/movies/features/"
    "best-movies-2/"
)

# Pega a pasta onde o programa está
pasta_programa = os.path.dirname(
    os.path.abspath(__file__)
)

# Define onde a lista será salva
caminho_arquivo = os.path.join(
    pasta_programa,
    "movies.txt"
)


# Busca o conteúdo da página
def buscar_pagina():
    try:
        resposta = requests.get(
            url=ENDERECO_SITE,
            timeout=20
        )

        resposta.raise_for_status()

        return resposta.text

    except requests.RequestException as erro:
        print("Não foi possível acessar o site.")
        print(erro)

        return None


# Procura os títulos dos filmes
def buscar_filmes(conteudo_pagina):
    site = BeautifulSoup(
        conteudo_pagina,
        "html.parser"
    )

    titulos_encontrados = site.find_all(
        name="h3",
        class_="title"
    )

    filmes = []

    for titulo in titulos_encontrados:
        nome_filme = titulo.get_text(
            strip=True
        )

        filmes.append(
            nome_filme
        )

    # A página mostra a lista do número 100 até o 1
    # Por isso, a lista precisa ser invertida
    filmes.reverse()

    return filmes


# Salva os filmes no arquivo de texto
def salvar_filmes(filmes):
    try:
        with open(
            caminho_arquivo,
            mode="w",
            encoding="utf-8"
        ) as arquivo:

            for filme in filmes:
                arquivo.write(
                    f"{filme}\n"
                )

        print("Lista criada com sucesso.")
        print(f"Quantidade de filmes: {len(filmes)}")
        print(f"Arquivo salvo em: {caminho_arquivo}")

    except OSError as erro:
        print("Não foi possível criar o arquivo.")
        print(erro)


# Inicia o programa
conteudo_pagina = buscar_pagina()

if conteudo_pagina is not None:
    lista_filmes = buscar_filmes(
        conteudo_pagina
    )

    if len(lista_filmes) > 0:
        salvar_filmes(
            lista_filmes
        )

    else:
        print("Nenhum filme foi encontrado na página.")