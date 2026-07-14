```python
from turtle import Turtle, Screen
import random
import time

# Configurações da cobra
POSICOES_INICIAIS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCIA_MOVIMENTO = 20

CIMA = 90
BAIXO = 270
ESQUERDA = 180
DIREITA = 0

# Configurações do placar
ALINHAMENTO = "center"
FONTE = ("Courier", 24, "normal")


class Cobra:

    def __init__(self):
        self.segmentos = []
        self.criar_cobra()
        self.cabeca = self.segmentos[0]

    # Cria os segmentos iniciais da cobra
    def criar_cobra(self):

        for posicao in POSICOES_INICIAIS:
            self.adicionar_segmento(posicao)

    # Adiciona uma nova parte ao corpo da cobra
    def adicionar_segmento(self, posicao):

        novo_segmento = Turtle("square")
        novo_segmento.color("white")
        novo_segmento.penup()
        novo_segmento.goto(posicao)

        self.segmentos.append(novo_segmento)

    # Aumenta o tamanho da cobra
    def aumentar(self):

        ultima_posicao = self.segmentos[-1].position()
        self.adicionar_segmento(ultima_posicao)

    # Move o corpo e a cabeça da cobra
    def mover(self):

        for numero_segmento in range(
            len(self.segmentos) - 1,
            0,
            -1
        ):
            nova_posicao_x = self.segmentos[
                numero_segmento - 1
            ].xcor()

            nova_posicao_y = self.segmentos[
                numero_segmento - 1
            ].ycor()

            self.segmentos[numero_segmento].goto(
                nova_posicao_x,
                nova_posicao_y
            )

        self.cabeca.forward(DISTANCIA_MOVIMENTO)

    # Muda a direção da cobra
    def subir(self):

        if self.cabeca.heading() != BAIXO:
            self.cabeca.setheading(CIMA)

    def descer(self):

        if self.cabeca.heading() != CIMA:
            self.cabeca.setheading(BAIXO)

    def virar_esquerda(self):

        if self.cabeca.heading() != DIREITA:
            self.cabeca.setheading(ESQUERDA)

    def virar_direita(self):

        if self.cabeca.heading() != ESQUERDA:
            self.cabeca.setheading(DIREITA)


class Comida(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

        self.atualizar_posicao()

    # Coloca a comida em uma posição aleatória
    def atualizar_posicao(self):

        posicao_x = random.randint(-280, 280)
        posicao_y = random.randint(-280, 280)

        self.goto(posicao_x, posicao_y)


class Placar(Turtle):

    def __init__(self):
        super().__init__()

        self.pontuacao = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

        self.atualizar_placar()

    # Mostra a pontuação atual
    def atualizar_placar(self):

        self.write(
            f"Pontuação: {self.pontuacao}",
            align=ALINHAMENTO,
            font=FONTE
        )

    # Mostra a mensagem de fim de jogo
    def fim_de_jogo(self):

        self.goto(0, 0)

        self.write(
            "FIM DE JOGO",
            align=ALINHAMENTO,
            font=FONTE
        )

    # Aumenta a pontuação em 1
    def aumentar_pontuacao(self):

        self.pontuacao += 1
        self.clear()
        self.atualizar_placar()


# Cria e configura a tela
tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor("black")
tela.title("Jogo da Cobra")
tela.tracer(0)

# Cria os objetos do jogo
cobra = Cobra()
comida = Comida()
placar = Placar()

# Configura os controles do teclado
tela.listen()
tela.onkey(cobra.subir, "Up")
tela.onkey(cobra.descer, "Down")
tela.onkey(cobra.virar_esquerda, "Left")
tela.onkey(cobra.virar_direita, "Right")

jogo_acontecendo = True

while jogo_acontecendo:

    tela.update()
    time.sleep(0.1)

    cobra.mover()

    # Verifica se a cobra encostou na comida
    if cobra.cabeca.distance(comida) < 15:
        comida.atualizar_posicao()
        cobra.aumentar()
        placar.aumentar_pontuacao()

    # Verifica se a cobra bateu na parede
    if (
        cobra.cabeca.xcor() > 280
        or cobra.cabeca.xcor() < -280
        or cobra.cabeca.ycor() > 280
        or cobra.cabeca.ycor() < -280
    ):
        jogo_acontecendo = False
        placar.fim_de_jogo()

    # Verifica se a cobra bateu no próprio corpo
    for segmento in cobra.segmentos[1:]:

        if cobra.cabeca.distance(segmento) < 10:
            jogo_acontecendo = False
            placar.fim_de_jogo()
            break

# Mantém a janela aberta
tela.exitonclick()
```
