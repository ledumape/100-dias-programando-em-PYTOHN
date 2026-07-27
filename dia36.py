import os
import requests
from twilio.rest import Client


# Ação e empresa que serão pesquisadas
NOME_ACAO = "TSLA"
NOME_EMPRESA = "Tesla Inc"

# Endereços das APIs
ENDERECO_ACOES = "https://www.alphavantage.co/query"
ENDERECO_NOTICIAS = "https://newsapi.org/v2/everything"

# Diferença mínima para buscar notícias
PORCENTAGEM_MINIMA = 5

# Chaves e dados guardados nas variáveis de ambiente
CHAVE_ALPHA_VANTAGE = os.environ.get(
    "CHAVE_ALPHA_VANTAGE"
)

CHAVE_NOTICIAS = os.environ.get(
    "CHAVE_NOTICIAS"
)

ID_CONTA_TWILIO = os.environ.get(
    "ID_CONTA_TWILIO"
)

TOKEN_TWILIO = os.environ.get(
    "TOKEN_TWILIO"
)

NUMERO_TWILIO = os.environ.get(
    "NUMERO_TWILIO"
)

MEU_NUMERO = os.environ.get(
    "MEU_NUMERO"
)


# Verifica se todas as configurações foram preenchidas
def verificar_configuracoes():
    configuracoes = [
        CHAVE_ALPHA_VANTAGE,
        CHAVE_NOTICIAS,
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


# Busca os preços da ação
def buscar_precos():
    parametros = {
        "function": "TIME_SERIES_DAILY",
        "symbol": NOME_ACAO,
        "apikey": CHAVE_ALPHA_VANTAGE
    }

    try:
        resposta = requests.get(
            url=ENDERECO_ACOES,
            params=parametros,
            timeout=15
        )

        resposta.raise_for_status()

        dados = resposta.json()

        if "Time Series (Daily)" not in dados:
            print("Não foi possível encontrar os preços da ação.")
            print(dados)

            return None

        return dados["Time Series (Daily)"]

    except requests.RequestException as erro:
        print("Erro ao consultar os preços da ação.")
        print(erro)

        return None


# Calcula a diferença entre os dois últimos pregões
def calcular_variacao(dados_precos):
    lista_precos = list(
        dados_precos.values()
    )

    if len(lista_precos) < 2:
        print("Não existem dados suficientes para calcular a variação.")

        return None

    fechamento_ontem = float(
        lista_precos[0]["4. close"]
    )

    fechamento_anteontem = float(
        lista_precos[1]["4. close"]
    )

    diferenca = (
        fechamento_ontem
        - fechamento_anteontem
    )

    porcentagem = (
        diferenca
        / fechamento_anteontem
    ) * 100

    porcentagem = round(
        porcentagem,
        2
    )

    if diferenca > 0:
        movimento = "SUBIU"

    elif diferenca < 0:
        movimento = "CAIU"

    else:
        movimento = "NÃO MUDOU"

    print(
        f"Fechamento mais recente: {fechamento_ontem}"
    )

    print(
        f"Fechamento anterior: {fechamento_anteontem}"
    )

    print(
        f"A ação {movimento} {abs(porcentagem)}%."
    )

    return porcentagem, movimento


# Busca notícias sobre a empresa
def buscar_noticias():
    parametros = {
        "apiKey": CHAVE_NOTICIAS,
        "qInTitle": NOME_EMPRESA,
        "language": "en",
        "sortBy": "publishedAt"
    }

    try:
        resposta = requests.get(
            url=ENDERECO_NOTICIAS,
            params=parametros,
            timeout=15
        )

        resposta.raise_for_status()

        dados = resposta.json()

        if dados.get("status") != "ok":
            print("Não foi possível buscar as notícias.")
            print(dados)

            return []

        artigos = dados.get(
            "articles",
            []
        )

        # Pega apenas as três primeiras notícias
        return artigos[:3]

    except requests.RequestException as erro:
        print("Erro ao consultar as notícias.")
        print(erro)

        return []


# Organiza o texto das notícias
def preparar_mensagens(
    artigos,
    porcentagem,
    movimento
):
    mensagens = []

    for artigo in artigos:
        titulo = artigo.get(
            "title",
            "Título não disponível"
        )

        descricao = artigo.get(
            "description",
            "Descrição não disponível"
        )

        mensagem = (
            f"{NOME_ACAO}: {movimento} "
            f"{abs(porcentagem)}%\n\n"
            f"Notícia: {titulo}\n\n"
            f"Resumo: {descricao}"
        )

        mensagens.append(
            mensagem
        )

    return mensagens


# Envia as mensagens pelo Twilio
def enviar_mensagens(mensagens):
    try:
        cliente = Client(
            ID_CONTA_TWILIO,
            TOKEN_TWILIO
        )

        for mensagem in mensagens:
            envio = cliente.messages.create(
                body=mensagem,
                from_=NUMERO_TWILIO,
                to=MEU_NUMERO
            )

            print("Mensagem enviada.")
            print(f"Situação: {envio.status}")

    except Exception as erro:
        print("Não foi possível enviar as mensagens.")
        print(erro)


# Inicia o programa
if verificar_configuracoes():
    dados_precos = buscar_precos()

    if dados_precos is not None:
        resultado = calcular_variacao(
            dados_precos
        )

        if resultado is not None:
            porcentagem, movimento = resultado

            if abs(porcentagem) >= PORCENTAGEM_MINIMA:
                print("Buscando notícias da empresa...")

                noticias = buscar_noticias()

                if len(noticias) > 0:
                    mensagens = preparar_mensagens(
                        noticias,
                        porcentagem,
                        movimento
                    )

                    enviar_mensagens(
                        mensagens
                    )

                else:
                    print("Nenhuma notícia foi encontrada.")

            else:
                print(
                    "A variação não foi suficiente "
                    "para buscar notícias."
                )