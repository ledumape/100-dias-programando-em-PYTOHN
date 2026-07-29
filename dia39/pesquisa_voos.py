import os
import requests
from dotenv import load_dotenv


# Carrega as informações do arquivo .env
load_dotenv()

ENDERECO_SERPAPI = "https://serpapi.com/search"


class PesquisaVoos:

    def __init__(self):
        self.chave_api = os.environ[
            "SERPAPI_API_KEY"
        ]

    # Pesquisa os voos
    def verificar_voos(
        self,
        codigo_origem,
        codigo_destino,
        data_ida,
        data_volta
    ):
        parametros = {
            "engine": "google_flights",
            "departure_id": codigo_origem,
            "arrival_id": codigo_destino,
            "outbound_date": data_ida.strftime(
                "%Y-%m-%d"
            ),
            "return_date": data_volta.strftime(
                "%Y-%m-%d"
            ),
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self.chave_api
        }

        try:
            resposta = requests.get(
                url=ENDERECO_SERPAPI,
                params=parametros,
                timeout=20
            )

            resposta.raise_for_status()

            dados = resposta.json()

            if "error" in dados:
                print(
                    f"Erro da API: {dados['error']}"
                )

                return None

            return dados

        except requests.RequestException as erro:
            print(
                "Não foi possível pesquisar os voos."
            )
            print(erro)

            return None