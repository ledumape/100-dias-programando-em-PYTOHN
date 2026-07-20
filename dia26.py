
# Dicionário com o alfabeto fonético da OTAN
alfabeto_fonetico = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliet",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"
}


# Transforma uma palavra no alfabeto fonético
def transformar_palavra(palavra):
    lista_fonetica = []

    for letra in palavra:

        # Verifica se o caractere é uma letra válida
        if letra in alfabeto_fonetico:
            lista_fonetica.append(alfabeto_fonetico[letra])

        # Mantém os espaços entre as palavras
        elif letra == " ":
            lista_fonetica.append("ESPAÇO")

        else:
            print(f"O caractere '{letra}' não é válido.")

    return lista_fonetica


continuar = True

while continuar:

    palavra_usuario = input(
        "\nDigite uma palavra ou frase: "
    ).upper()

    resultado = transformar_palavra(palavra_usuario)

    print("\nResultado:")
    print(resultado)

    # Mostra o resultado de forma mais fácil de ler
    print("\nAlfabeto fonético:")
    print(" - ".join(resultado))

    resposta = input(
        "\nDeseja escrever outra palavra? Digite 'sim' ou 'não': "
    ).lower()

    if resposta == "não" or resposta == "nao":
        continuar = False
        print("Programa encerrado.")
