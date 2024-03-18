import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''




escolha =  int(input("Escolha um numero para jogar pedra,papel e tesoura: 0 para pedra, 1 para tesoura e 2 para papel"))
lista2 = [pedra, tesoura, papel]
lista = ["pedra", "tesoura", "papel"]

computador_escolha = random.choice(lista)

if escolha >2:
  print("voce escolheu um numero invalido, voce perdeu")
elif escolha == 0 and computador_escolha == "papel":
  print(f"o computador venceu o computador botou {papel} e voce botou\n {lista2[escolha]}")
elif escolha == 1 and computador_escolha == "papel":
  print(f"Voce ganhou computador botou {papel}  voce botou\n {lista2[escolha]}")
elif escolha == 2 and computador_escolha == "tesoura":
  print(f"computador vence computador botou {tesoura}  voce botou\n {lista2[escolha]}")
elif escolha == 1 and computador_escolha == "pedra":
  print(f"computador venceu computador botou {pedra}  voce botou\n {lista2[escolha]}")
elif escolha == 2 and computador_escolha == "pedra":
  print(f"voce ganhou computador botou {pedra}  voce botou:\n {lista2[escolha]}")
elif escolha == 0 and computador_escolha == "tesoura":
  print(f"voce ganhou computador botou: {tesoura}  voce botou:\n {lista2[escolha]}")
else:
  print(f"empatou!!!!! computador botou: {computador_escolha}  voce botou:\n {lista2[escolha]}")