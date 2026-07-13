from turtle import Turtle, Screen
import random

# Controla se a corrida está acontecendo
corrida_acontecendo = False

# Cria e configura a tela
tela = Screen()
tela.setup(width=500, height=400)

# Pergunta em qual tartaruga o usuário deseja apostar
aposta_usuario = tela.textinput(
    title="Faça sua aposta",
    prompt="Qual tartaruga vai ganhar? Digite uma cor: "
)

cores = ["red", "orange", "yellow", "green", "blue", "purple"]
posicoes_y = [-70, -40, -10, 20, 50, 80]

todas_tartarugas = []

# Cria as 6 tartarugas
for numero_tartaruga in range(6):

    nova_tartaruga = Turtle(shape="turtle")
    nova_tartaruga.penup()
    nova_tartaruga.color(cores[numero_tartaruga])

    nova_tartaruga.goto(
        x=-230,
        y=posicoes_y[numero_tartaruga]
    )

    todas_tartarugas.append(nova_tartaruga)

# Inicia a corrida se o usuário fizer uma aposta
if aposta_usuario:
    aposta_usuario = aposta_usuario.lower()
    corrida_acontecendo = True

# Mantém a corrida funcionando até uma tartaruga vencer
while corrida_acontecendo:

    for tartaruga in todas_tartarugas:

        # Verifica se a tartaruga chegou ao final
        if tartaruga.xcor() > 230:

            corrida_acontecendo = False
            cor_vencedora = tartaruga.pencolor()

            if cor_vencedora == aposta_usuario:
                print(
                    f"Você ganhou! A tartaruga "
                    f"{cor_vencedora} venceu a corrida!"
                )
            else:
                print(
                    f"Você perdeu! A tartaruga "
                    f"{cor_vencedora} venceu a corrida!"
                )

            break

        # Faz a tartaruga andar uma distância aleatória
        distancia_aleatoria = random.randint(0, 10)
        tartaruga.forward(distancia_aleatoria)

# Mantém a tela aberta até o usuário clicar
tela.exitonclick()