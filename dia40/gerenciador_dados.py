import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


# Carrega as variáveis do arquivo .env
load_dotenv()

ENDERECO_PRECOS = os.environ[
    "SHEETY_PRICES_ENDPOINT"
]


class GerenciadorDados:

    def __init__(self):
        usuario = os.environ[
            "SHEETY_USERNAME"
        ]

        senha = os.environ[
            "SHEETY_PASSWORD"
        ]

        self.autorizacao = HTTPBasicAuth(
            usuario,
            senha
        )

        self.endereco_clientes = os.environ[
            "SHEETY_USERS_ENDPOINT"
        ]

        self.destinos = []
        self.clientes = []

    # Busca os destinos da planilha
    def buscar_destinos(self):
        try:
            resposta = requests.get(
                url=ENDERECO_PRECOS,
                auth=self.autorizacao,
                timeout=15
            )

            resposta.raise_for_status()

            dados = resposta.json()

            self.destinos = dados["prices"]

            return self.destinos

        except requests.RequestException as erro:
            print(
                "Não foi possível buscar os destinos."
            )

            print(erro)

            return []

    # Atualiza o menor preço
    def atualizar_menor_preco(
        self,
        id_linha,
        novo_preco
    ):
        novos_dados = {
            "price": {
                "lowestPrice": novo_preco
            }
        }

        try:
            resposta = requests.put(
                url=f"{ENDERECO_PRECOS}/{id_linha}",
                json=novos_dados,
                auth=self.autorizacao,
                timeout=15
            )

            resposta.raise_for_status()

            print(
                "Preço atualizado na planilha."
            )

        except requests.RequestException as erro:
            print(
                "Não foi possível atualizar o preço."
            )

            print(erro)

    # Busca os clientes cadastrados
    def buscar_clientes(self):
        try:
            resposta = requests.get(
                url=self.endereco_clientes,
                auth=self.autorizacao,
                timeout=15
            )

            resposta.raise_for_status()

            dados = resposta.json()

            self.clientes = dados["users"]

            return self.clientes

        except requests.RequestException as erro:
            print(
                "Não foi possível buscar os clientes."
            )

            print(erro)

            return []