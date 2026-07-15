
from turtle import Turtle, Screen
import time


class Raquete(Turtle):

    def __init__(self, posicao):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(posicao)

    # Move a raquete para cima
    def subir(self):
        nova_posicao_y = self.ycor() + 20
        self.goto(self.xcor(), nova_posicao_y)

    # Move a raquete para baixo
    def descer(self):
        nova_posicao_y = self.ycor() - 20
        self.goto(self.xcor(), nova_posicao_y)


class Bola(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.shape("circle")
        self.penup()

        self.movimento_x = 3
        self.movimento_y = 3
        self.velocidade = 0.01

    # Move a bola pela tela
    def mover(self):
        nova_posicao_x = self.xcor() + self.movimento_x
        nova_posicao_y = self.ycor() + self.movimento_y

        self.goto(nova_posicao_x, nova_posicao_y)

    # Faz a bola rebater nas paredes de cima e de baixo
    def rebater_vertical(self):
        self.movimento_y *= -1

    # Faz a bola rebater nas raquetes
    def rebater_horizontal(self):
        self.movimento_x *= -1

        # Aumenta a velocidade da bola
        self.velocidade *= 0.9

    # Coloca a bola novamente no centro
    def reiniciar_posicao(self):
        self.goto(0, 0)
        self.velocidade = 0.01
        self.rebater_horizontal()


class Placar(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()

        self.pontos_esquerda = 0
        self.pontos_direita = 0

        self.atualizar_placar()

    # Mostra os pontos dos dois jogadores
    def atualizar_placar(self):
        self.clear()

        self.goto(-100, 200)
        self.write(
            self.pontos_esquerda,
            align="center",
            font=("Courier", 80, "normal")
        )

        self.goto(100, 200)
        self.write(
            self.pontos_direita,
            align="center",
            font=("Courier", 80, "normal")
        )

    # Adiciona um ponto ao jogador da esquerda
    def ponto_esquerda(self):
        self.pontos_esquerda += 1
        self.atualizar_placar()

    # Adiciona um ponto ao jogador da direita
    def ponto_direita(self):
        self.pontos_direita += 1
        self.atualizar_placar()


# Cria e configura a tela
tela = Screen()
tela.bgcolor("black")
tela.setup(width=800, height=600)
tela.title("Jogo Pong")
tela.tracer(0)

# Cria as duas raquetes
raquete_direita = Raquete((350, 0))
raquete_esquerda = Raquete((-350, 0))

# Cria a bola e o placar
bola = Bola()
placar = Placar()

# Configura os controles
tela.listen()

tela.onkey(raquete_direita.subir, "Up")
tela.onkey(raquete_direita.descer, "Down")

tela.onkey(raquete_esquerda.subir, "w")
tela.onkey(raquete_esquerda.descer, "s")

jogo_acontecendo = True

while jogo_acontecendo:
    time.sleep(bola.velocidade)

    tela.update()
    bola.mover()

    # Verifica a colisão com as paredes
    if bola.ycor() > 280 or bola.ycor() < -280:
        bola.rebater_vertical()

    # Verifica a colisão com a raquete da direita
    if (
        bola.distance(raquete_direita) < 50
        and bola.xcor() > 320
    ):
        bola.rebater_horizontal()

    # Verifica a colisão com a raquete da esquerda
    if (
        bola.distance(raquete_esquerda) < 50
        and bola.xcor() < -320
    ):
        bola.rebater_horizontal()

    # A raquete da direita perdeu a bola
    if bola.xcor() > 380:
        bola.reiniciar_posicao()
        placar.ponto_esquerda()

    # A raquete da esquerda perdeu a bola
    if bola.xcor() < -380:
        bola.reiniciar_posicao()
        placar.ponto_direita()

# Mantém a tela aberta
tela.exitonclick()
