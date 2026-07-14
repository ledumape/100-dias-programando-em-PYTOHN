```python
from turtle import Turtle, Screen
import time

# Posições iniciais das partes da cobra
POSICOES_INICIAIS = [(0, 0), (-20, 0), (-40, 0)]

# Distância que a cobra anda
DISTANCIA_MOVIMENTO = 20

# Direções da cobra
CIMA = 90
BAIXO = 270
ESQUERDA = 180
DIREITA = 0


class Cobra:

    def __init__(self):
        self.segmentos = []

        # Cria o corpo da cobra
        self.criar_cobra()

        # O primeiro segmento será a cabeça
        self.cabeca = self.segmentos[0]

    # Cria os três segmentos iniciais
    def criar_cobra(self):

        for posicao in POSICOES_INICIAIS:
            novo_segmento = Turtle("square")
            novo_segmento.color("white")
            novo_segmento.penup()
            novo_segmento.goto(posicao)

            self.segmentos.append(novo_segmento)

    # Faz os segmentos seguirem a cabeça
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

        # Move a cabeça para frente
        self.cabeca.forward(DISTANCIA_MOVIMENTO)

    # Muda a direção para cima
    def subir(self):

        if self.cabeca.heading() != BAIXO:
            self.cabeca.setheading(CIMA)

    # Muda a direção para baixo
    def descer(self):

        if self.cabeca.heading() != CIMA:
            self.cabeca.setheading(BAIXO)

    # Muda a direção para esquerda
    def virar_esquerda(self):

        if self.cabeca.heading() != DIREITA:
            self.cabeca.setheading(ESQUERDA)

    # Muda a direção para direita
    def virar_direita(self):

        if self.cabeca.heading() != ESQUERDA:
            self.cabeca.setheading(DIREITA)


# Cria e configura a tela do jogo
tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor("black")
tela.title("Jogo da Cobra")
tela.tracer(0)

# Cria a cobra
cobra = Cobra()

# Configura as teclas do teclado
tela.listen()
tela.onkey(cobra.subir, "Up")
tela.onkey(cobra.descer, "Down")
tela.onkey(cobra.virar_esquerda, "Left")
tela.onkey(cobra.virar_direita, "Right")

jogo_acontecendo = True

# Mantém o jogo funcionando
while jogo_acontecendo:
    tela.update()
    time.sleep(0.1)

    cobra.mover()

# Mantém a tela aberta até o usuário clicar
tela.exitonclick()
```
