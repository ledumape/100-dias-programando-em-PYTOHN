import requests
from datetime import datetime, timezone
import smtplib
import time


# Dados do seu e-mail
MEU_EMAIL = "SEU_EMAIL@gmail.com"
MINHA_SENHA = "SUA_SENHA_DE_APLICATIVO"

# Servidor SMTP do Gmail
SERVIDOR_SMTP = "smtp.gmail.com"

# Localização de Brasília
MINHA_LATITUDE = -15.793889
MINHA_LONGITUDE = -47.882778


# Verifica se a Estação Espacial está próxima
def estacao_esta_proxima():
    try:
        resposta = requests.get(
            url="http://api.open-notify.org/iss-now.json",
            timeout=10
        )

        resposta.raise_for_status()

        dados = resposta.json()

        latitude_estacao = float(
            dados["iss_position"]["latitude"]
        )

        longitude_estacao = float(
            dados["iss_position"]["longitude"]
        )

        # Considera próxima dentro de 5 graus
        latitude_proxima = (
            MINHA_LATITUDE - 5
            <= latitude_estacao
            <= MINHA_LATITUDE + 5
        )

        longitude_proxima = (
            MINHA_LONGITUDE - 5
            <= longitude_estacao
            <= MINHA_LONGITUDE + 5
        )

        if latitude_proxima and longitude_proxima:
            return True

        return False

    except requests.RequestException as erro:
        print("Erro ao verificar a posição da estação.")
        print(erro)

        return False


# Verifica se está de noite
def esta_de_noite():
    parametros = {
        "lat": MINHA_LATITUDE,
        "lng": MINHA_LONGITUDE,
        "formatted": 0
    }

    try:
        resposta = requests.get(
            url="https://api.sunrise-sunset.org/json",
            params=parametros,
            timeout=10
        )

        resposta.raise_for_status()

        dados = resposta.json()

        horario_nascer_sol = datetime.fromisoformat(
            dados["results"]["sunrise"]
        )

        horario_por_sol = datetime.fromisoformat(
            dados["results"]["sunset"]
        )

        horario_atual = datetime.now(
            timezone.utc
        )

        # Está de noite antes do nascer ou depois do pôr do sol
        if (
            horario_atual <= horario_nascer_sol
            or horario_atual >= horario_por_sol
        ):
            return True

        return False

    except requests.RequestException as erro:
        print("Erro ao verificar o horário do sol.")
        print(erro)

        return False


# Envia o aviso por e-mail
def enviar_email():
    try:
        with smtplib.SMTP(
            SERVIDOR_SMTP,
            587
        ) as conexao:

            conexao.starttls()

            conexao.login(
                MEU_EMAIL,
                MINHA_SENHA
            )

            mensagem = (
                "Subject:Estacao Espacial acima de voce\n\n"
                "A Estacao Espacial Internacional esta "
                "passando perto da sua localizacao.\n"
                "Olhe para o ceu."
            )

            conexao.sendmail(
                from_addr=MEU_EMAIL,
                to_addrs=MEU_EMAIL,
                msg=mensagem.encode("utf-8")
            )

        print("E-mail enviado com sucesso.")

    except smtplib.SMTPAuthenticationError:
        print("Não foi possível entrar no e-mail.")
        print("Verifique o e-mail e a senha de aplicativo.")

    except Exception as erro:
        print("Ocorreu um erro ao enviar o e-mail.")
        print(erro)


# Repete a verificação a cada 60 segundos
while True:
    print("Verificando a posição da estação...")

    if estacao_esta_proxima() and esta_de_noite():
        enviar_email()

        # Espera mais tempo para não enviar vários e-mails seguidos
        time.sleep(600)

    else:
        print("A estação não está visível neste momento.")

        time.sleep(60)