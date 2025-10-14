def calculadora():
    print("Operações disponíveis:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    escolha = input("Qual operação você deseja? (1/2/3/4): ")
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    
    if escolha == "1":
        print("Resultado:", n1 + n2)
    elif escolha == "2":
        print("Resultado:", n1 - n2)
    elif escolha == "3":
        print("Resultado:", n1 * n2)
    elif escolha == "4":
        if n2 != 0:
            print("Resultado:", n1 / n2)
        else:
            print("Erro! Divisão por zero não é permitida.")
    else:
        print("Operação inválida.")

calculadora()
