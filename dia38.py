import requests
from datetime import datetime
import os


# Dados pessoais usados para calcular as calorias
SEXO = "male"
PESO_KG = 84
ALTURA_CM = 180
IDADE = 32


# Chaves da API
ID_APLICATIVO = os.environ["ENV_NIX_APP_ID"]
CHAVE_API = os.environ["ENV_NIX_API_KEY"]

# Endereço da API de exercícios
ENDERECO_EXERCICIOS = (
    "https://app.100daysofpython.dev/v1/"
    "nutrition/natural/exercise"
)

# Endereço da planilha pelo Sheety
ENDERECO_PLANILHA = os.environ[
    "ENV_SHEETY_ENDPOINT"
]

# Nome usado pelo Sheety
NOME_PLANILHA = "workout"


# Busca as informações do exercício
def buscar_exercicio():
    exercicio_digitado = input(
        "Quais exercícios você fez hoje? "
    )

    cabecalho = {
        "x-app-id": ID_APLICATIVO,
        "x-app-key": CHAVE_API
    }

    dados = {
        "query": exercicio_digitado,
        "gender": SEXO,
        "weight_kg": PESO_KG,
        "height_cm": ALTURA_CM,
        "age": IDADE
    }

    try:
        resposta = requests.post(
            url=ENDERECO_EXERCICIOS,
            json=dados,
            headers=cabecalho,
            timeout=15
        )

        resposta.raise_for_status()

        resultado = resposta.json()

        return resultado

    except requests.RequestException as erro:
        print("Não foi possível buscar os exercícios.")
        print(erro)

        return None


# Salva os exercícios na planilha
def salvar_na_planilha(resultado):
    data_atual = datetime.now().strftime(
        "%d/%m/%Y"
    )

    hora_atual = datetime.now().strftime(
        "%H:%M:%S"
    )

    for exercicio in resultado["exercises"]:
        dados_planilha = {
            NOME_PLANILHA: {
                "date": data_atual,
                "time": hora_atual,
                "exercise": exercicio["name"].title(),
                "duration": exercicio["duration_min"],
                "calories": exercicio["nf_calories"]
            }
        }

        try:
            resposta = requests.post(
                url=ENDERECO_PLANILHA,
                json=dados_planilha,
                auth=(
                    os.environ["ENV_SHEETY_USERNAME"],
                    os.environ["ENV_SHEETY_PASSWORD"]
                ),
                timeout=15
            )

            resposta.raise_for_status()

            print(
                f"{exercicio['name'].title()} "
                "foi salvo na planilha."
            )

        except requests.RequestException as erro:
            print(
                "Não foi possível salvar o exercício "
                "na planilha."
            )

            print(erro)


# Inicia o programa
resultado_exercicios = buscar_exercicio()

if resultado_exercicios is not None:
    if len(resultado_exercicios["exercises"]) > 0:
        salvar_na_planilha(
            resultado_exercicios
        )

        print("Exercícios registrados com sucesso.")

    else:
        print("Nenhum exercício foi encontrado.")