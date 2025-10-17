moedas_validas = [1, 5, 10, 25]
precos = {'espresso': 150, 'latte': 250, 'cappuccino': 300}

agua = 300
po_cafe = 100
leite = 200

cafe = input("Qual Café? (espresso/latte/cappuccino): ").lower()

while True:
    match cafe:
        case 'espresso':
            if agua < 50 or po_cafe < 18:
                print("não tem recursos para espresso")
                break

            print("Preço: R$1,50")
            total = 0
            for moeda in moedas_validas:
                qtd = int(input(f"Quantas moedas de {moeda} centavos? "))
                total += moeda * qtd

            if total < precos['espresso']:
                print("Dinheiro insuficiente!")
                break
            if total > precos['espresso']:
                print(f"Troco: {total - precos['espresso']} centavos")

            agua -= 50
            po_cafe -= 18
            print("aqui está o espresso")
            cafe = input("Qual Café? ").lower()

        case 'latte':
            if agua < 200 or po_cafe < 24 or leite < 150:
                print("não tem recursos para latte")
                break

            print("Preço: R$2,50")
            total = 0
            for moeda in moedas_validas:
                qtd = int(input(f"Quantas moedas de {moeda} centavos? "))
                total += moeda * qtd

            if total < precos['latte']:
                print("Dinheiro insuficiente!")
                break
            if total > precos['latte']:
                print(f"Troco: {total - precos['latte']} centavos")

            agua -= 200
            po_cafe -= 24
            leite -= 150
            print("aqui está o latte")
            cafe = input("Qual Café? ").lower()

        case 'cappuccino':
            if agua < 250 or po_cafe < 24 or leite < 100:
                print("não tem recursos para cappuccino")
                break

            print("Preço: R$3,00")
            total = 0
            for moeda in moedas_validas:
                qtd = int(input(f"Quantas moedas de {moeda} centavos? "))
                total += moeda * qtd

            if total < precos['cappuccino']:
                print("Dinheiro insuficiente!")
                break
            if total > precos['cappuccino']:
                print(f"Troco: {total - precos['cappuccino']} centavos")

            agua -= 250
            po_cafe -= 24
            leite -= 100
            print("aqui está o cappuccino")
            cafe = input("Qual Café? ").lower()

        case 'desligar':
            print("desligando...")
            break

        case 'status':
            print(f"pó de café: {po_cafe}, leite: {leite}, água: {agua}")
            cafe = input("Qual Café? ").lower()

        case _:
            print("Opção inválida")
            cafe = input("Qual Café? ").lower()
