import smtplib
import datetime
import random
import os

# Dados do seu e-mail
MEU_EMAIL = "SEU_EMAIL@gmail.com"
MINHA_SENHA = "SUA_SENHA_DE_APLICATIVO"

# E-mail que receberá a mensagem
EMAIL_DESTINO = "EMAIL_DESTINO@gmail.com"

# Servidor utilizado pelo Gmail
SERVIDOR_SMTP = "smtp.gmail.com"

# Pega a pasta onde o programa está
pasta_programa = os.path.dirname(
    os.path.abspath(__file__)
)

# Caminho do arquivo de frases
caminho_frases = os.path.join(
    pasta_programa,
    "quotes.txt"
)


# Escolhe uma frase aleatória
def escolher_frase():
    try:
        with open(
            caminho_frases,
            mode="r",
            encoding="utf-8"
        ) as arquivo:

            frases = arquivo.readlines()

    except FileNotFoundError:
        print("O arquivo quotes.txt não foi encontrado.")
        return None

    if len(frases) == 0:
        print("O arquivo quotes.txt está vazio.")
        return None

    frase = random.choice(frases)

    return frase.strip()


# Envia a frase por e-mail
def enviar_email(frase):
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
                "Subject:Motivacao da semana\n\n"
                f"{frase}"
            )

            conexao.sendmail(
                from_addr=MEU_EMAIL,
                to_addrs=EMAIL_DESTINO,
                msg=mensagem.encode("utf-8")
            )

        print("E-mail enviado com sucesso.")

    except smtplib.SMTPAuthenticationError:
        print("Não foi possível entrar no e-mail.")
        print("Verifique o endereço e a senha de aplicativo.")

    except Exception as erro:
        print("Ocorreu um erro ao enviar o e-mail.")
        print(erro)


# Verifica o dia atual
hoje = datetime.datetime.now()

dia_semana = hoje.weekday()

# Segunda-feira é representada pelo número 0
if dia_semana == 0:
    frase_escolhida = escolher_frase()

    if frase_escolhida is not None:
        enviar_email(frase_escolhida)

else:
    print("Hoje não é segunda-feira.")