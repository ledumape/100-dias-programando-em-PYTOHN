from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)


ofertas = {}
dole3 = False

def maior_oferta(numero_ofertas):
  melhor_oferta=0
  vencedor = ""
  for oferta in numero_ofertas:
   quantidade_ofertas=numero_ofertas[oferta]
   if quantidade_ofertas > melhor_oferta:
     melhor_oferta = quantidade_ofertas
     vencedor = oferta
  print(f"O vencedor é {vencedor} com a oferta de {melhor_oferta}")
  


while not dole3:
  nome = input("qual o seu nome?")
  preço = int(input("qual é sua oferta? $"))
  ofertas[nome] = preço
  continuar = input("tem mais alguem para apostar? sim ou não?")
  if continuar == "nao":
    dole3 = True
    maior_oferta(ofertas)
  elif continuar == "sim":
    clear()
    
  