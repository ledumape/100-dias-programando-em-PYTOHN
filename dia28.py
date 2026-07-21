
from tkinter import *
import math
import os

# Cores usadas no programa
ROSA = "#e2979c"
VERMELHO = "#e7305b"
VERDE = "#9bdeac"
AMARELO = "#f7f5dd"

FONTE = "Courier"

# Tempo de cada etapa em minutos
TEMPO_TRABALHO = 1
PAUSA_CURTA = 5
PAUSA_LONGA = 20

repeticoes = 0
temporizador = None


# Reinicia o temporizador
def reiniciar_temporizador():
    global repeticoes
    global temporizador

    # Cancela a contagem caso ela esteja funcionando
    if temporizador is not None:
        janela.after_cancel(temporizador)

    repeticoes = 0
    temporizador = None

    texto_tempo.itemconfig(numero_tempo, text="00:00")
    titulo.config(text="Temporizador", fg=VERDE)
    marcacoes.config(text="")


# Inicia uma nova etapa do Pomodoro
def iniciar_temporizador():
    global repeticoes

    repeticoes += 1

    segundos_trabalho = TEMPO_TRABALHO * 60
    segundos_pausa_curta = PAUSA_CURTA * 60
    segundos_pausa_longa = PAUSA_LONGA * 60

    # A cada 4 períodos de trabalho, inicia uma pausa longa
    if repeticoes % 8 == 0:
        titulo.config(text="Pausa longa", fg=VERMELHO)
        contagem_regressiva(segundos_pausa_longa)

    # Depois de cada período de trabalho, inicia uma pausa curta
    elif repeticoes % 2 == 0:
        titulo.config(text="Pausa", fg=ROSA)
        contagem_regressiva(segundos_pausa_curta)

    # Inicia o período de trabalho
    else:
        titulo.config(text="Trabalho", fg=VERDE)
        contagem_regressiva(segundos_trabalho)


# Faz a contagem regressiva
def contagem_regressiva(contagem):
    global temporizador

    minutos = math.floor(contagem / 60)
    segundos = contagem % 60

    # Coloca um zero antes dos segundos menores que 10
    if segundos < 10:
        segundos = f"0{segundos}"

    texto_tempo.itemconfig(
        numero_tempo,
        text=f"{minutos}:{segundos}"
    )

    if contagem > 0:
        temporizador = janela.after(
            1000,
            contagem_regressiva,
            contagem - 1
        )

    else:
        iniciar_temporizador()

        marcas = ""
        periodos_concluidos = math.floor(repeticoes / 2)

        # Adiciona uma marca para cada período concluído
        for _ in range(periodos_concluidos):
            marcas += "✔"

        marcacoes.config(text=marcas)


# Pega o caminho da pasta onde o programa está
pasta_programa = os.path.dirname(
    os.path.abspath(__file__)
)

caminho_imagem = os.path.join(
    pasta_programa,
    "tomato.png"
)

# Verifica se a imagem está na pasta
if not os.path.exists(caminho_imagem):
    print("A imagem tomato.png não foi encontrada.")
    print(f"Coloque a imagem nesta pasta: {pasta_programa}")
    exit()


# Cria e configura a janela
janela = Tk()
janela.title("Pomodoro")
janela.config(
    padx=100,
    pady=50,
    bg=AMARELO
)


# Título do temporizador
titulo = Label(
    text="Temporizador",
    fg=VERDE,
    bg=AMARELO,
    font=(FONTE, 40)
)

titulo.grid(
    column=1,
    row=0
)


# Área que mostra a imagem e o tempo
texto_tempo = Canvas(
    width=200,
    height=224,
    bg=AMARELO,
    highlightthickness=0
)

imagem_tomate = PhotoImage(
    file=caminho_imagem
)

texto_tempo.create_image(
    100,
    112,
    image=imagem_tomate
)

numero_tempo = texto_tempo.create_text(
    100,
    130,
    text="00:00",
    fill="white",
    font=(FONTE, 35, "bold")
)

texto_tempo.grid(
    column=1,
    row=1
)


# Botão para iniciar
botao_iniciar = Button(
    text="Iniciar",
    command=iniciar_temporizador,
    highlightthickness=0
)

botao_iniciar.grid(
    column=0,
    row=2
)


# Botão para reiniciar
botao_reiniciar = Button(
    text="Reiniciar",
    command=reiniciar_temporizador,
    highlightthickness=0
)

botao_reiniciar.grid(
    column=2,
    row=2
)


# Mostra os períodos de trabalho concluídos
marcacoes = Label(
    text="",
    fg=VERDE,
    bg=AMARELO,
    font=(FONTE, 18)
)

marcacoes.grid(
    column=1,
    row=3
)


# Mantém a janela aberta
janela.mainloop()
