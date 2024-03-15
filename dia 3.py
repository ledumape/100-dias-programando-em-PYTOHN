print("Voce entrou em uma aventura para achar o o bau do tesouro vamos ver se voce consegue fazer as escolhas certas para chegar ate ele\n")

primeira=input("voce esta em uma floresta maluca voce tem que escolher entre ir para esquerda ou direita qual voce escolhe? D/E? ")
if primeira =="E":
  print("parabens voce fez a escolha certa, voce sobreviveu")
  segunda = input("voce chegou em um porto e precisa escolher entre nada ou esperar o barco, qual voce escolhe? N/E? ")
  if segunda == "E":
    print("parabens voce fez a escolha certa voce espera o barco e vai tranquilamenta para ilha ")
    terceira = input("voce chegou na ilha e precisa escolher entre 3 portas : vermelha, amarela e azul qual voce escolhe? V/A/Z?")

    if terceira == "V":
      print("voce caiu em um buraco e morreu")
    elif terceira == "A":
      print("ganhou ganhou ganhou o bau do tesouro")
    else:
      print("voce tava em chamas e morreu")
  else:
    print("voce foi atacado por um tubarao e morreu")
    
else:
  print("voce foi comido por macacos famintos, voce morreu")


