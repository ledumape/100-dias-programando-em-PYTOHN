import os
import requests
from twilio.rest import Client


# Endereço da API de previsão do tempo
ENDERECO_PREVISAO = (
    "https://api.openweathermap.org/data/2.5/forecast"
)

# Dados do OpenWeather
CHAVE_OPENWEATHER = os.environ.get(
    "CHAVE_OPENWEATHER"
)

# Dados da conta Twilio
ID_CONTA_TWILIO = os.environ.get(
    "ID_CONTA_TWILIO"
)

TOKEN_TWILIO = os.environ.get(
    "TOKEN_TWILIO"
)

# Números de telefone
NUMERO_TWILIO = os.environ.get(
    "NUMERO_TWILIO"
)

MEU_NUMERO = os.environ.get(
    "MEU_NUMERO"
)

# Localização de Brasília
MINHA_LATITUDE = -15.793889
MINHA_LONGITUDE = -47.882778


# Busca a previsão do tempo
def buscar_previsao():
    parametros = {
        "lat": MINHA_LATITUDE,
        "lon": MINHA_LONGITUDE,
        "appid": CHAVE_OPENWEATHER,
        "cnt": 4
    }

    try:
        resposta = requests.get(
            url=ENDERECO_PREVISAO,
            params=parametros,
            timeout=10
        )

        resposta.raise_for_status()

        return resposta.json()

    except requests.RequestException as erro:
        print("Não foi possível consultar a previsão.")
        print(erro)

        return None


# Verifica se pode chover
def verificar_chuva(dados_previsao):
    for horario in dados_previsao["list"]:
        codigo_clima = horario["weather"][0]["id"]

        # Códigos menores que 700 representam chuva,
        # tempestade, garoa ou neve
        if codigo_clima < 700:
            return True

    return False


# Envia uma mensagem pelo Twilio
def enviar_mensagem():
    try:
        cliente = Client(
            ID_CONTA_TWILIO,
            TOKEN_TWILIO
        )

        mensagem = cliente.messages.create(
            body=(
                "Há possibilidade de chuva nas próximas "
                "horas. Lembre-se de levar um guarda-chuva."
            ),
            from_=NUMERO_TWILIO,
            to=MEU_NUMERO
        )

        print("Mensagem enviada.")
        print(f"Situação: {mensagem.status}")

    except Exception as erro:
        print("Não foi possível enviar a mensagem.")
        print(erro)


# Verifica se as configurações foram preenchidas
def verificar_configuracoes():
    configuracoes = [
        CHAVE_OPENWEATHER,
        ID_CONTA_TWILIO,
        TOKEN_TWILIO,
        NUMERO_TWILIO,
        MEU_NUMERO
    ]

    if None in configuracoes:
        print("Existem configurações que não foram preenchidas.")
        print("Verifique as variáveis de ambiente.")

        return False

    return True


# Inicia o programa
if verificar_configuracoes():
    previsao = buscar_previsao()

    if previsao is not None:
        vai_chover = verificar_chuva(
            previsao
        )

        if vai_chover:
            print("Há possibilidade de chuva.")
            enviar_mensagem()

        else:
            print("Não há previsão de chuva.")