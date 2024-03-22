Python
import random

fases = [
    '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
       |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    /|\  |
    /   |
       |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    /|\  |
       |
       |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    /|   |
       |
       |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    |   |
       |
       |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
       |
       |
       |
    =========
    ''',
    '''
    +---+
    |   |
       |
       |
       |
       |
    =========
    '''
]

mostra = []
word_list = ["aardvark", "balao", "camelo"]
palavra_escolhida = random.choice(word_list)
tamanho = len(palavra_escolhida)
game_over = False
vidas = 6

for _ in range(tamanho):
    mostra += "_"


print(palavra_escolhida)
while not game_over:

    tentativa = input("Qual letra você quer tentar?").lower()

    for posicao in range(tamanho):
        letra = palavra_escolhida[posicao]

        if letra == tentativa:
            mostra[posicao] = letra

    if tentativa not in palavra_escolhida:
        vidas -= 1
        if vidas == 0:
            game_over = True
            print("Você perdeu!")

    print(f"{' '.join(mostra)}")

    if "_" not in mostra:
        game_over = True
        print("Você ganhou!")

    print(fases[vidas])
