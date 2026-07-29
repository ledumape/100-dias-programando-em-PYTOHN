import smtplib
import os
from dotenv import load_dotenv
from twilio.rest import Client


# Carrega o arquivo .env
load_dotenv()


class GerenciadorNotificacoes:

    def __init__(self):
        self.servidor_email = os.environ[
            "EMAIL_PROVIDER_SMTP_ADDRESS"
        ]

        self.meu_email = os.environ[
            "MY_EMAIL"
        ]

        self.senha_email = os.environ[
            "MY_EMAIL_PASSWORD"
        ]

        self.cliente_twilio = Client(
            os.environ["TWILIO_SID"],
            os.environ["TWILIO_AUTH_TOKEN"]
        )

    # Envia SMS
    def enviar_sms(self, mensagem):
        envio = self.cliente_twilio.messages.create(
            from_=os.environ[
                "TWILIO_VIRTUAL_NUMBER"
            ],
            body=mensagem,
            to=os.environ[
                "TWILIO_VERIFIED_NUMBER"
            ]
        )

        print(
            f"SMS enviado: {envio.sid}"
        )

    # Envia mensagem pelo WhatsApp
    def enviar_whatsapp(self, mensagem):
        envio = self.cliente_twilio.messages.create(
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
            f"WhatsApp enviado: {envio.sid}"
        )

    # Envia e-mails para todos os clientes
    def enviar_emails(
        self,
        lista_emails,
        mensagem
    ):
        try:
            with smtplib.SMTP(
                self.servidor_email
            ) as conexao:

                conexao.starttls()

                conexao.login(
                    self.meu_email,
                    self.senha_email
                )

                for email in lista_emails:
                    conexao.sendmail(
                        from_addr=self.meu_email,
                        to_addrs=email,
                        msg=(
                            "Subject:Alerta de voo barato!\n\n"
                            f"{mensagem}"
                        ).encode("utf-8")
                    )

                    print(
                        f"E-mail enviado para {email}."
                    )

        except Exception as erro:
            print(
                "Não foi possível enviar os e-mails."
            )

            print(erro)