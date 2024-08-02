


def soma(n1, n2):
  return n1+n2 

def subração(n1,n2):
  return n1-n2

def multiplicação(n1,n2):
  return n1*n2

def divisão(n1,n2):
  return n1/n2

operadores = {
  "+":soma,
  "-": subração,
  "*": multiplicação,
  "/": divisão
}

def calculadora():

  
  num1 = float(input("Qual o primeiro número? "))
  for simbulo in operadores:
    print(simbulo)
    



  verdade = True
  while verdade:
    simbulo_escolido = input("Escolha uma operação:")
    num2 = float(input("Qual o proximo número? "))
    simbolo_operacao = operadores[simbulo_escolido]
    resposta1 = simbolo_operacao(num1 , num2)
      
    print(f"{num1} {simbulo_escolido} {num2} = {resposta1}")
    if input(f"voce deseja continuar sua conta com o numero {resposta1} se sim digite 's' se não digite 'n'")=="s":
      num1 = resposta1
    else:
      verdade= False
      calculadora()


calculadora()
