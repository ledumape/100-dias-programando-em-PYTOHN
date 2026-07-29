import os
from dotenv import load_dotenv
from twilio.rest import Client


# Carrega as informações do arquivo .env
load_dotenv()


class GerenciadorNotificacoes:

    def __init__(self):
        self.cliente = Client(
            os.environ["TWILIO_SID"],
            os.environ["TWILIO_AUTH_TOKEN"]
        )

    # Envia uma mensagem SMS
    def enviar_sms(
        self,
        mensagem
    ):
        envio = self.cliente.messages.create(
            from_=os.environ[
                "TWILIO_VIRTUAL_NUMBER"
            ],
            body=mensagem,
            to=os.environ[
                "TWILIO_VERIFIED_NUMBER"
            ]
        )

        print(
            f"Mensagem enviada: {envio.sid}"
        )

    # Envia uma mensagem pelo WhatsApp
    def enviar_whatsapp(
        self,
        mensagem
    ):
        envio = self.cliente.messages.create(
            from_=(
                "whatsapp:"
                + os.environ[
                    "TWILIO_WHATSAPP_NUMBER"
                ]
            ),
            body=mensagem,
            to=(
                "whatsapp:"
                + os.environ[
                    "TWILIO_VERIFIED_NUMBER"
                ]
            )
        )

        print(
            f"Mensagem enviada: {envio.sid}"
        )