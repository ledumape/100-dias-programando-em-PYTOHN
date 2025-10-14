import os
import random
os.system('cls' if os.name == 'nt' else 'clear')

numero_pc= random.randrange(0,100)

modo_jogo = input("qual modo de jogo quer jogar? FACIL OU DIFICIL? ")
numero = int(input("qual numero voce acha que ele esta pensando? "))
vidas = 0
if modo_jogo.lower() == "facil":
    vidas =10
else:
    vidas = 5
    
while vidas != 0:
    if numero > numero_pc:
        print("muito alto")
        vidas -=1
        print("voce tem", vidas)
    elif numero < numero_pc:
        print("muito baixo")
        vidas -=1
        print("voce tem", vidas)
    else:
        print("voce ganhou")
        break
    numero = int(input("qual numero voce acha que ele esta pensando? "))


