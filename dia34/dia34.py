
from tkinter import *
from tkinter import messagebox
import requests
import html
import os


# Cor principal do programa
COR_TEMA = "#375362"

# Quantidade de perguntas do quiz
QUANTIDADE_PERGUNTAS = 10


# Pega a pasta onde o programa está
pasta_programa = os.path.dirname(
    os.path.abspath(__file__)
)

# Caminhos das imagens
caminho_imagem_certo = os.path.join(
    pasta_programa,
    "images",
    "true.png"
)

caminho_imagem_errado = os.path.join(
    pasta_programa,
    "images",
    "false.png"
)


# Guarda uma pergunta e sua resposta
class Pergunta:

    def __init__(self, texto, resposta):
        self.texto = texto
        self.resposta = resposta


# Controla as perguntas e a pontuação
class Quiz:

    def __init__(self, lista_perguntas):
        self.numero_pergunta = 0
        self.pontuacao = 0
        self.lista_perguntas = lista_perguntas
        self.pergunta_atual = None

    # Verifica se ainda existem perguntas
    def ainda_tem_perguntas(self):
        return (
            self.numero_pergunta
            < len(self.lista_perguntas)
        )

    # Retorna a próxima pergunta
    def proxima_pergunta(self):
        self.pergunta_atual = self.lista_perguntas[
            self.numero_pergunta
        ]

        self.numero_pergunta += 1

        texto_pergunta = html.unescape(
            self.pergunta_atual.texto
        )

        return (
            f"Pergunta {self.numero_pergunta}:\n\n"
            f"{texto_pergunta}"
        )

    # Confere a resposta do usuário
    def verificar_resposta(self, resposta_usuario):
        resposta_correta = self.pergunta_atual.resposta

        if (
            resposta_usuario.lower()
            == resposta_correta.lower()
        ):
            self.pontuacao += 1
            return True

        return False


# Busca as perguntas na internet
def buscar_perguntas():
    parametros = {
        "amount": QUANTIDADE_PERGUNTAS,
        "type": "boolean"
    }

    try:
        resposta = requests.get(
            url="https://opentdb.com/api.php",
            params=parametros,
            timeout=10
        )

        resposta.raise_for_status()

        dados = resposta.json()

        if dados["response_code"] != 0:
            messagebox.showerror(
                title="Erro",
                message="A API não conseguiu fornecer as perguntas."
            )

            return []

        return dados["results"]

    except requests.RequestException as erro:
        messagebox.showerror(
            title="Erro de conexão",
            message=(
                "Não foi possível buscar as perguntas.\n\n"
                "Verifique sua conexão com a internet.\n\n"
                f"Erro: {erro}"
            )
        )

        return []


# Transforma os dados em objetos do tipo Pergunta
def criar_banco_perguntas(dados_perguntas):
    banco_perguntas = []

    for dados in dados_perguntas:
        texto = dados["question"]
        resposta = dados["correct_answer"]

        nova_pergunta = Pergunta(
            texto,
            resposta
        )

        banco_perguntas.append(
            nova_pergunta
        )

    return banco_perguntas


# Mostra a próxima pergunta na tela
def mostrar_proxima_pergunta():
    area_pergunta.config(
        bg="white"
    )

    if quiz.ainda_tem_perguntas():
        texto_pontuacao.config(
            text=f"Pontuação: {quiz.pontuacao}"
        )

        pergunta = quiz.proxima_pergunta()

        area_pergunta.itemconfig(
            texto_pergunta,
            text=pergunta,
            fill=COR_TEMA
        )

    else:
        area_pergunta.itemconfig(
            texto_pergunta,
            text=(
                "Você chegou ao final do quiz.\n\n"
                f"Pontuação final: "
                f"{quiz.pontuacao}/"
                f"{len(quiz.lista_perguntas)}"
            ),
            fill=COR_TEMA
        )

        texto_pontuacao.config(
            text=f"Pontuação final: {quiz.pontuacao}"
        )

        botao_certo.config(
            state=DISABLED
        )

        botao_errado.config(
            state=DISABLED
        )


# Executa quando o usuário clica em verdadeiro
def resposta_verdadeiro():
    resposta_certa = quiz.verificar_resposta(
        "True"
    )

    mostrar_resultado(
        resposta_certa
    )


# Executa quando o usuário clica em falso
def resposta_falso():
    resposta_certa = quiz.verificar_resposta(
        "False"
    )

    mostrar_resultado(
        resposta_certa
    )


# Mostra se o usuário acertou ou errou
def mostrar_resultado(resposta_certa):
    if resposta_certa:
        area_pergunta.config(
            bg="green"
        )

    else:
        area_pergunta.config(
            bg="red"
        )

    janela.after(
        1000,
        mostrar_proxima_pergunta
    )


# Verifica se as imagens existem
def verificar_imagens():
    if not os.path.exists(caminho_imagem_certo):
        messagebox.showerror(
            title="Imagem não encontrada",
            message=(
                "A imagem true.png não foi encontrada.\n\n"
                "Coloque a imagem dentro da pasta images."
            )
        )

        return False

    if not os.path.exists(caminho_imagem_errado):
        messagebox.showerror(
            title="Imagem não encontrada",
            message=(
                "A imagem false.png não foi encontrada.\n\n"
                "Coloque a imagem dentro da pasta images."
            )
        )

        return False

    return True


# Cria a janela principal
janela = Tk()
janela.title("Quizzler")
janela.config(
    padx=20,
    pady=20,
    bg=COR_TEMA
)


# Verifica os arquivos necessários
if not verificar_imagens():
    janela.destroy()

else:
    # Busca as perguntas na internet
    dados_perguntas = buscar_perguntas()

    if len(dados_perguntas) == 0:
        janela.destroy()

    else:
        # Cria o banco de perguntas
        banco_perguntas = criar_banco_perguntas(
            dados_perguntas
        )

        # Cria o controle do quiz
        quiz = Quiz(
            banco_perguntas
        )

        # Mostra a pontuação
        texto_pontuacao = Label(
            text="Pontuação: 0",
            fg="white",
            bg=COR_TEMA,
            font=("Arial", 12, "bold")
        )

        texto_pontuacao.grid(
            row=0,
            column=1,
            sticky="e"
        )

        # Área branca onde a pergunta aparece
        area_pergunta = Canvas(
            width=300,
            height=250,
            bg="white",
            highlightthickness=0
        )

        texto_pergunta = area_pergunta.create_text(
            150,
            125,
            width=270,
            text="Carregando pergunta...",
            fill=COR_TEMA,
            font=("Arial", 18, "italic"),
            justify="center"
        )

        area_pergunta.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=50
        )

        # Carrega as imagens dos botões
        imagem_certo = PhotoImage(
            file=caminho_imagem_certo
        )

        imagem_errado = PhotoImage(
            file=caminho_imagem_errado
        )

        # Botão verdadeiro
        botao_certo = Button(
            image=imagem_certo,
            highlightthickness=0,
            borderwidth=0,
            command=resposta_verdadeiro
        )

        botao_certo.grid(
            row=2,
            column=0
        )

        # Botão falso
        botao_errado = Button(
            image=imagem_errado,
            highlightthickness=0,
            borderwidth=0,
            command=resposta_falso
        )

        botao_errado.grid(
            row=2,
            column=1
        )

        # Mostra a primeira pergunta
        mostrar_proxima_pergunta()


# Mantém a janela aberta
janela.mainloop()