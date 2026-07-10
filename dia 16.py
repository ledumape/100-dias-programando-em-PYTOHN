# Recursos iniciais da máquina
recursos = {
    "agua": 300,
    "leite": 200,
    "cafe": 100
}

# Dinheiro acumulado pela máquina
dinheiro = 0

# Ingredientes e preços de cada bebida
bebidas = {
    "espresso": {
        "agua": 50,
        "leite": 0,
        "cafe": 18,
        "preco": 1.50
    },
    "latte": {
        "agua": 200,
        "leite": 150,
        "cafe": 24,
        "preco": 2.50
    },
    "cappuccino": {
        "agua": 250,
        "leite": 100,
        "cafe": 24,
        "preco": 3.00
    }
}


# Mostra os recursos disponíveis na máquina
def mostrar_relatorio():
    print("\nRELATÓRIO DA MÁQUINA")
    print(f"Água: {recursos['agua']} ml")
    print(f"Leite: {recursos['leite']} ml")
    print(f"Café: {recursos['cafe']} g")
    print(f"Dinheiro: R$ {dinheiro:.2f}")


# Verifica se existem ingredientes suficientes
def verificar_recursos(bebida):
    if recursos["agua"] < bebida["agua"]:
        print("Desculpe, não há água suficiente.")
        return False

    elif recursos["leite"] < bebida["leite"]:
        print("Desculpe, não há leite suficiente.")
        return False

    elif recursos["cafe"] < bebida["cafe"]:
        print("Desculpe, não há café suficiente.")
        return False

    else:
        return True


# Pergunta quantas moedas o cliente inseriu
def processar_moedas():
    print("\nInsira as moedas.")

    moedas_25 = int(input("Quantas moedas de 25 centavos? "))
    moedas_10 = int(input("Quantas moedas de 10 centavos? "))
    moedas_5 = int(input("Quantas moedas de 5 centavos? "))
    moedas_1 = int(input("Quantas moedas de 1 centavo? "))

    total = moedas_25 * 0.25
    total += moedas_10 * 0.10
    total += moedas_5 * 0.05
    total += moedas_1 * 0.01

    return total


# Retira os ingredientes usados e entrega a bebida
def fazer_cafe(nome_bebida, bebida):
    recursos["agua"] -= bebida["agua"]
    recursos["leite"] -= bebida["leite"]
    recursos["cafe"] -= bebida["cafe"]

    print(f"Aqui está o seu {nome_bebida}. Aproveite!")


maquina_ligada = True

while maquina_ligada:

    escolha = input(
        "\nO que você gostaria? (espresso/latte/cappuccino): "
    ).lower()

    # Desliga a máquina
    if escolha == "desligar":
        maquina_ligada = False
        print("Máquina de café desligada.")

    # Mostra o relatório dos recursos
    elif escolha == "relatorio":
        mostrar_relatorio()

    # Verifica se a bebida escolhida existe
    elif escolha in bebidas:
        bebida_escolhida = bebidas[escolha]

        tem_recursos = verificar_recursos(bebida_escolhida)

        if tem_recursos:
            valor_inserido = processar_moedas()
            preco = bebida_escolhida["preco"]

            print(f"Valor inserido: R$ {valor_inserido:.2f}")
            print(f"Preço da bebida: R$ {preco:.2f}")

            # Verifica se o dinheiro é suficiente
            if valor_inserido < preco:
                print("Desculpe, o dinheiro não é suficiente.")
                print("Dinheiro devolvido.")

            else:
                dinheiro += preco

                troco = valor_inserido - preco
                troco = round(troco, 2)

                # Mostra o troco quando necessário
                if troco > 0:
                    print(f"Aqui está R$ {troco:.2f} de troco.")

                fazer_cafe(escolha, bebida_escolhida)

    else:
        print("Opção inválida.")
        print("Escolha espresso, latte, cappuccino, relatório ou desligar.")
