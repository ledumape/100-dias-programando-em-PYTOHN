import random
resposta = ""
def dar_cartas():
    #escolhe uma carta 
    cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    cartao=random.choice(cartas)
    return cartao




cartas_usurario = []


cartas_computador = []
 

for tempo in range(2):
     cartas_usurario.append(dar_cartas())
     cartas_computador.append(dar_cartas())


print("suas cartas sao:",(cartas_usurario))
print("as do computador sao:",(cartas_computador))

resposta = input("voce quer mais cartas?")

while resposta.lower() == "s":
    cartas_usurario.append(dar_cartas())
    print("suas cartas sao", cartas_usurario)
    soma = sum(cartas_usurario)
    print("\nsuas cartas estao dando:", soma)
    
    
    while soma > 21 and 11 in cartas_usurario:
        for i in range(len(cartas_usurario)):
            if cartas_usurario[i] == 11:
                resposta_ás = input("Você quer que o Ás valha 1? (s/n) ")
                if resposta_ás.lower() == "s":
                    cartas_usurario[i] = 1
                    soma = sum(cartas_usurario)
                    print("Nova soma:", soma)
                break  
    
    if soma > 21:
        print("você estourou!")
        break
    resposta = input("voce quer mais cartas?\n")


     
while sum(cartas_computador) < 17:
    cartas_computador.append(dar_cartas())



soma_usuario=(sum(cartas_usurario))
soma_computador=(sum(cartas_computador))
if soma_computador > 21:
     print("O usuario ganhou")

elif soma_computador > 21:
     print("O usuario ganhou")

elif soma_usuario < soma_computador:
     print("o computador ganhou")
 
elif soma_computador < soma_usuario:
     print("o usuario  ganhou")
else:
     print("empatou") 


print(soma_usuario)
print(soma_computador)