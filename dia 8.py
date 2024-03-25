alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def ceasr(texto_comeco, chave_cript, direcao_cesar):
  texto_final =""
  if direcao_cesar == "decode":
    chave_cript *= -1
  for char in texto_comeco:
    if char in alfabeto:
      posicao = alfabeto.index(char)
      nova_posicao = posicao + (chave_cript)
      texto_final += alfabeto[nova_posicao]
    else:
      texto_final += char
      
      
    
  print(f"the {direcao_cesar}d text is {texto_final}")

contiua = True

while contiua: 
  direcao = input("escreva encrypt para encripitar e decode para desencripitar:\n")
  texto = input("escreva sua mensagem:\n").lower()
  chave = int(input("digite o numero da chave:\n"))


  chave = chave % 26
  ceasr(texto_comeco=texto, chave_cript=chave, direcao_cesar=direcao)
  repitir = input("quer continuar? escreva sim ou nao:\n")
  if repitir == "nao":
    chave = False
    print("vlw")