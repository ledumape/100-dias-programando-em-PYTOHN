#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Bem vindo a calculadora de gorjetas!")
conta = (float(input("qual foi o valor da conta? ")))
gorjeta = int(input("qual a porcentagem da gorjeta? 10%, 12% ou 15% "))
pessoas = int(input("quantas pessoas vao dividir a conta? "))
gorjeta_porcentagem = gorjeta/100
gorjeta_total = conta * gorjeta_porcentagem
conta_total = conta + gorjeta_total
conta_por_pessoa = conta_total/ pessoas
final = round(conta_por_pessoa,2)
final = "{:.2f}".format(conta_por_pessoa)
print(f"cada pessoa deve pegar: R${final}")