import turtle
import random

# Permite usar cores no formato RGB
turtle.colormode(255)

# Cria a tartaruga que vai fazer o desenho
pincel = turtle.Turtle()
pincel.speed("fastest")
pincel.penup()
pincel.hideturtle()

# Lista de cores disponíveis
lista_cores = [
    (202, 164, 109),
    (238, 240, 245),
    (150, 75, 49),
    (223, 201, 135),
    (52, 93, 124),
    (172, 154, 40),
    (140, 30, 19),
    (133, 163, 185),
    (198, 91, 71),
    (46, 122, 86),
    (72, 43, 35),
    (145, 178, 148),
    (13, 99, 71),
    (233, 175, 164),
    (161, 142, 158),
    (105, 74, 77),
    (55, 46, 50),
    (183, 205, 171),
    (36, 60, 74),
    (18, 86, 90),
    (81, 148, 129),
    (148, 17, 20),
    (14, 70, 64),
    (30, 68, 100),
    (107, 127, 153),
    (174, 94, 97),
    (176, 192, 209)
]

# Posiciona a tartaruga no canto inferior esquerdo
pincel.setheading(225)
pincel.forward(300)
pincel.setheading(0)

quantidade_bolinhas = 100

# Desenha 100 bolinhas em uma grade de 10 por 10
for numero_bolinha in range(1, quantidade_bolinhas + 1):

    cor_escolhida = random.choice(lista_cores)

    pincel.dot(20, cor_escolhida)
    pincel.forward(50)

    # A cada 10 bolinhas, passa para a linha de cima
    if numero_bolinha % 10 == 0:
        pincel.setheading(90)
        pincel.forward(50)

        pincel.setheading(180)
        pincel.forward(500)

        pincel.setheading(0)

# Mantém a janela aberta até o usuário clicar
tela = turtle.Screen()
tela.exitonclick()