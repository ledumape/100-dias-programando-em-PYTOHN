
from turtle import Turtle, Screen
import random
import time

# Configurações do jogador
POSICAO_INICIAL = (0, -280)
DISTANCIA_MOVIMENTO = 10
LINHA_CHEGADA = 280

# Configurações dos carros
CORES = ["red", "orange", "yellow", "green", "blue", "purple"]
VELOCIDADE_INICIAL = 5
AUMENTO_VELOCIDADE = 10

# Configuração do placar
FONTE = ("Courier", 24, "normal")


class Jogador(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.ir_para_inicio()
        self.setheading(90)

    # Move o jogador para cima
    def subir(self):
        self.forward(DISTANCIA_MOVIMENTO)

    # Coloca o jogador na posição inicial
    def ir_para_inicio(self):
        self.goto(POSICAO_INICIAL)

    # Verifica se o jogador chegou ao final
    def chegou_na_chegada(self):

        if self.ycor() > LINHA_CHEGADA:
            return True
        else:
            return False


class GerenciadorCarros:

    def __init__(self):
        self.todos_carros = []
        self.velocidade_carros = VELOCIDADE_INICIAL

    # Cria carros em posições aleatórias
    def criar_carro(self):

        chance_aleatoria = random.randint(1, 6)

        if chance_aleatoria == 1:
            novo_carro = Turtle("square")
            novo_carro.shapesize(stretch_wid=1, stretch_len=2)
            novo_carro.penup()
            novo_carro.color(random.choice(CORES))

            posicao_y = random.randint(-250, 250)

            novo_carro.goto(300, posicao_y)

            self.todos_carros.append(novo_carro)

    # Move todos os carros para a esquerda
    def mover_carros(self):

        for carro in self.todos_carros:
            carro.backward(self.velocidade_carros)

    # Aumenta a velocidade dos carros
    def aumentar_nivel(self):
        self.velocidade_carros += AUMENTO_VELOCIDADE


class Placar(Turtle):

    def __init__(self):
        super().__init__()

        self.nivel = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)

        self.atualizar_placar()

    # Mostra o nível atual
    def atualizar_placar(self):
        self.clear()

        self.write(
            f"Nível: {self.nivel}",
            align="left",
            font=FONTE
        )

    # Aumenta o nível do jogo
    def aumentar_nivel(self):
        self.nivel += 1
        self.atualizar_placar()

    # Mostra a mensagem de fim de jogo
    def fim_de_jogo(self):
        self.goto(0, 0)

        self.write(
            "FIM DE JOGO",
            align="center",
            font=FONTE
        )


# Cria e configura a tela
tela = Screen()
tela.setup(width=600, height=600)
tela.title("Travessia da Tartaruga")
tela.tracer(0)

# Cria os objetos do jogo
jogador = Jogador()
gerenciador_carros = GerenciadorCarros()
placar = Placar()

# Configura o controle do jogador
tela.listen()
tela.onkey(jogador.subir, "Up")

jogo_acontecendo = True

while jogo_acontecendo:
    time.sleep(0.1)
    tela.update()

    # Cria e movimenta os carros
    gerenciador_carros.criar_carro()
    gerenciador_carros.mover_carros()

    # Verifica se o jogador bateu em algum carro
    for carro in gerenciador_carros.todos_carros:

        if carro.distance(jogador) < 20:
            jogo_acontecendo = False
            placar.fim_de_jogo()
            break

    # Verifica se o jogador chegou ao outro lado
    if jogador.chegou_na_chegada():
        jogador.ir_para_inicio()
        gerenciador_carros.aumentar_nivel()
        placar.aumentar_nivel()

# Mantém a tela aberta
tela.exitonclick()