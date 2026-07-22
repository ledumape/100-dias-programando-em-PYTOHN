from tkinter import *
from tkinter import messagebox
import random
import csv
import os

# Cor de fundo do programa
COR_FUNDO = "#B1DDC6"

# Guarda a carta que está sendo mostrada
carta_atual = {}

# Guarda as palavras que ainda precisam ser aprendidas
palavras_para_aprender = []

# Guarda o temporizador que vira a carta
temporizador = None


# Pega a pasta onde o programa está
pasta_programa = os.path.dirname(
    os.path.abspath(__file__)
)

# Caminhos das imagens
caminho_frente = os.path.join(
    pasta_programa,
    "images",
    "card_front.png"
)

caminho_verso = os.path.join(
    pasta_programa,
    "images",
    "card_back.png"
)

caminho_certo = os.path.join(
    pasta_programa,
    "images",
    "right.png"
)

caminho_errado = os.path.join(
    pasta_programa,
    "images",
    "wrong.png"
)

# Caminhos dos arquivos de palavras
caminho_palavras_originais = os.path.join(
    pasta_programa,
    "data",
    "french_words.csv"
)

caminho_palavras_restantes = os.path.join(
    pasta_programa,
    "data",
    "words_to_learn.csv"
)


# Carrega as palavras do arquivo CSV
def carregar_palavras():
    global palavras_para_aprender

    try:
        # Primeiro tenta abrir as palavras restantes
        with open(
            caminho_palavras_restantes,
            mode="r",
            encoding="utf-8"
        ) as arquivo:

            leitor = csv.DictReader(arquivo)
            palavras_para_aprender = list(leitor)

    except FileNotFoundError:
        try:
            # Caso ainda não exista, abre a lista original
            with open(
                caminho_palavras_originais,
                mode="r",
                encoding="utf-8"
            ) as arquivo:

                leitor = csv.DictReader(arquivo)
                palavras_para_aprender = list(leitor)

        except FileNotFoundError:
            messagebox.showerror(
                title="Arquivo não encontrado",
                message=(
                    "O arquivo french_words.csv não foi encontrado.\n\n"
                    "Coloque o arquivo dentro da pasta data."
                )
            )

            janela.destroy()


# Mostra uma nova palavra
def proxima_carta():
    global carta_atual
    global temporizador

    # Cancela o temporizador anterior
    if temporizador is not None:
        janela.after_cancel(temporizador)

    # Verifica se ainda existem palavras
    if len(palavras_para_aprender) == 0:
        area_carta.itemconfig(
            titulo_carta,
            text="Parabéns",
            fill="black"
        )

        area_carta.itemconfig(
            palavra_carta,
            text="Você aprendeu todas as palavras",
            fill="black",
            font=("Arial", 28, "bold")
        )

        area_carta.itemconfig(
            fundo_carta,
            image=imagem_frente
        )

        botao_certo.config(state=DISABLED)
        botao_errado.config(state=DISABLED)

        return

    # Escolhe uma palavra aleatória
    carta_atual = random.choice(
        palavras_para_aprender
    )

    # Mostra o lado francês
    area_carta.itemconfig(
        titulo_carta,
        text="Francês",
        fill="black"
    )

    area_carta.itemconfig(
        palavra_carta,
        text=carta_atual["French"],
        fill="black",
        font=("Arial", 60, "bold")
    )

    area_carta.itemconfig(
        fundo_carta,
        image=imagem_frente
    )

    # Vira a carta depois de 3 segundos
    temporizador = janela.after(
        3000,
        virar_carta
    )


# Mostra a tradução em inglês
def virar_carta():
    area_carta.itemconfig(
        titulo_carta,
        text="Inglês",
        fill="white"
    )

    area_carta.itemconfig(
        palavra_carta,
        text=carta_atual["English"],
        fill="white"
    )

    area_carta.itemconfig(
        fundo_carta,
        image=imagem_verso
    )


# Salva as palavras que ainda precisam ser aprendidas
def salvar_palavras():
    with open(
        caminho_palavras_restantes,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        nomes_colunas = [
            "French",
            "English"
        ]

        escritor = csv.DictWriter(
            arquivo,
            fieldnames=nomes_colunas
        )

        escritor.writeheader()
        escritor.writerows(
            palavras_para_aprender
        )


# Remove uma palavra já conhecida
def palavra_conhecida():
    if carta_atual in palavras_para_aprender:
        palavras_para_aprender.remove(
            carta_atual
        )

        salvar_palavras()

    proxima_carta()


# Verifica se os arquivos de imagem existem
def verificar_imagens():
    imagens = [
        caminho_frente,
        caminho_verso,
        caminho_certo,
        caminho_errado
    ]

    for caminho in imagens:
        if not os.path.exists(caminho):
            messagebox.showerror(
                title="Imagem não encontrada",
                message=(
                    "Uma imagem do projeto não foi encontrada:\n\n"
                    f"{caminho}"
                )
            )

            janela.destroy()
            return False

    return True


# Cria a janela principal
janela = Tk()
janela.title("Cartões de Memorização")
janela.config(
    padx=50,
    pady=50,
    bg=COR_FUNDO
)


# Verifica os arquivos antes de continuar
if verificar_imagens():

    # Carrega as imagens
    imagem_frente = PhotoImage(
        file=caminho_frente
    )

    imagem_verso = PhotoImage(
        file=caminho_verso
    )

    imagem_certo = PhotoImage(
        file=caminho_certo
    )

    imagem_errado = PhotoImage(
        file=caminho_errado
    )


    # Cria a área da carta
    area_carta = Canvas(
        width=800,
        height=526,
        bg=COR_FUNDO,
        highlightthickness=0
    )

    fundo_carta = area_carta.create_image(
        400,
        263,
        image=imagem_frente
    )

    titulo_carta = area_carta.create_text(
        400,
        150,
        text="",
        font=("Arial", 40, "italic")
    )

    palavra_carta = area_carta.create_text(
        400,
        263,
        text="",
        font=("Arial", 60, "bold"),
        width=650
    )

    area_carta.grid(
        row=0,
        column=0,
        columnspan=2
    )


    # Botão para informar que não conhece a palavra
    botao_errado = Button(
        image=imagem_errado,
        highlightthickness=0,
        borderwidth=0,
        command=proxima_carta
    )

    botao_errado.grid(
        row=1,
        column=0
    )


    # Botão para informar que conhece a palavra
    botao_certo = Button(
        image=imagem_certo,
        highlightthickness=0,
        borderwidth=0,
        command=palavra_conhecida
    )

    botao_certo.grid(
        row=1,
        column=1
    )


    # Carrega as palavras e inicia o programa
    carregar_palavras()

    if len(palavras_para_aprender) > 0:
        proxima_carta()


# Mantém a janela aberta
janela.mainloop()