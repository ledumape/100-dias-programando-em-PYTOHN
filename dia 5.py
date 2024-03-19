
import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao gerador de senha")
numero_letras= int(input("Quantas letras voce gostaria?\n")) 
numero_simbulos = int(input(f"Quantos simbulos voce gostaria?\n"))
numero_numeros= int(input(f"Quantos numeros voce gostaria?\n"))

teste = []


for coisa in range(0,numero_letras):  
  teste.append((random.choice(letras)))

for coisa1 in range(0,numero_numeros):
  teste.append(random.choice(numeros))

for coisa2 in range(0,numero_simbulos):
  teste.append(random.choice(simbolos))




random.shuffle(teste)
teste2 =" ".join(teste)

print(teste2)