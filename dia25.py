
import turtle

# Nome da imagem do mapa
IMAGEM_MAPA = "blank_states_img.gif"

# Dados dos estados e suas posições no mapa
estados = {
    "Alabama": (139, -77),
    "Alaska": (-204, -170),
    "Arizona": (-203, -40),
    "Arkansas": (57, -53),
    "California": (-297, 13),
    "Colorado": (-112, 20),
    "Connecticut": (297, 96),
    "Delaware": (275, 42),
    "Florida": (220, -145),
    "Georgia": (182, -75),
    "Hawaii": (-317, -143),
    "Idaho": (-216, 122),
    "Illinois": (95, 37),
    "Indiana": (133, 39),
    "Iowa": (38, 65),
    "Kansas": (-17, 5),
    "Kentucky": (149, 1),
    "Louisiana": (59, -114),
    "Maine": (319, 164),
    "Maryland": (288, 27),
    "Massachusetts": (312, 112),
    "Michigan": (148, 101),
    "Minnesota": (23, 135),
    "Mississippi": (94, -78),
    "Missouri": (49, 6),
    "Montana": (-141, 150),
    "Nebraska": (-61, 66),
    "Nevada": (-257, 56),
    "New Hampshire": (302, 127),
    "New Jersey": (282, 65),
    "New Mexico": (-128, -43),
    "New York": (236, 104),
    "North Carolina": (239, -22),
    "North Dakota": (-44, 158),
    "Ohio": (176, 52),
    "Oklahoma": (-8, -41),
    "Oregon": (-278, 138),
    "Pennsylvania": (238, 72),
    "Rhode Island": (318, 94),
    "South Carolina": (218, -51),
    "South Dakota": (-44, 109),
    "Tennessee": (131, -34),
    "Texas": (-38, -106),
    "Utah": (-189, 34),
    "Vermont": (282, 154),
    "Virginia": (234, 12),
    "Washington": (-257, 193),
    "West Virginia": (200, 20),
    "Wisconsin": (83, 113),
    "Wyoming": (-134, 90)
}


# Escreve o nome do estado na posição correta
def escrever_estado(nome_estado):
    posicao_x, posicao_y = estados[nome_estado]

    escritor = turtle.Turtle()
    escritor.hideturtle()
    escritor.penup()
    escritor.goto(posicao_x, posicao_y)
    escritor.write(
        nome_estado,
        align="center",
        font=("Arial", 8, "normal")
    )


# Salva os estados que o jogador ainda não acertou
def salvar_estados_faltando(estados_acertados):
    estados_faltando = []

    for estado in estados:
        if estado not in estados_acertados:
            estados_faltando.append(estado)

    with open(
        "estados_para_aprender.txt",
        mode="w",
        encoding="utf-8"
    ) as arquivo:

        for estado in estados_faltando:
            arquivo.write(estado + "\n")

    print("Os estados que faltaram foram salvos.")
    print("Arquivo: estados_para_aprender.txt")


# Cria e configura a tela
tela = turtle.Screen()
tela.title("Jogo dos Estados dos Estados Unidos")

# Coloca a imagem do mapa na tela
tela.addshape(IMAGEM_MAPA)
turtle.shape(IMAGEM_MAPA)

estados_acertados = []

# Continua enquanto o jogador não acertar todos os estados
while len(estados_acertados) < 50:

    resposta = tela.textinput(
        title=f"{len(estados_acertados)}/50 estados corretos",
        prompt="Digite o nome de outro estado ou 'sair':"
    )

    # Fecha o jogo caso o usuário feche a caixa de texto
    if resposta is None:
        salvar_estados_faltando(estados_acertados)
        break

    resposta = resposta.strip().title()

    # Encerra o jogo e salva os estados que faltaram
    if resposta == "Sair":
        salvar_estados_faltando(estados_acertados)
        break

    # Verifica se o estado existe e ainda não foi acertado
    if resposta in estados and resposta not in estados_acertados:
        estados_acertados.append(resposta)
        escrever_estado(resposta)

    elif resposta in estados_acertados:
        print(f"Você já acertou o estado {resposta}.")

    else:
        print("Estado inválido.")

# Mensagem quando o jogador acerta todos
if len(estados_acertados) == 50:
    print("Parabéns! Você acertou todos os estados.")

tela.exitonclick()
