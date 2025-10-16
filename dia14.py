import os
import random

os.system('cls' if os.name == 'nt' else 'clear')

pessoas = [
    {'nome': "Cristiano Ronaldo", 'instagram': "@cristiano", 'seguidores': 610, 'descrição': "Jogador de futebol profissional", 'país': "Portugal"},
    {'nome': "Lionel Messi", 'instagram': "@leomessi", 'seguidores': 495, 'descrição': "Jogador argentino e ídolo do futebol mundial", 'país': "Argentina"},
    {'nome': "Kylie Jenner", 'instagram': "@kyliejenner", 'seguidores': 400, 'descrição': "Empresária e influenciadora digital", 'país': "Estados Unidos"},
    {'nome': "Selena Gomez", 'instagram': "@selenagomez", 'seguidores': 428, 'descrição': "Cantora e atriz norte-americana", 'país': "Estados Unidos"},
    {'nome': "Dwayne Johnson", 'instagram': "@therock", 'seguidores': 395, 'descrição': "Ator e ex-lutador profissional", 'país': "Estados Unidos"},
    {'nome': "Kim Kardashian", 'instagram': "@kimkardashian", 'seguidores': 363, 'descrição': "Empresária e personalidade da mídia", 'país': "Estados Unidos"},
    {'nome': "Ariana Grande", 'instagram': "@arianagrande", 'seguidores': 380, 'descrição': "Cantora e atriz norte-americana", 'país': "Estados Unidos"},
    {'nome': "Taylor Swift", 'instagram': "@taylorswift", 'seguidores': 285, 'descrição': "Cantora e compositora", 'país': "Estados Unidos"},
    {'nome': "Beyoncé", 'instagram': "@beyonce", 'seguidores': 260, 'descrição': "Cantora e atriz", 'país': "Estados Unidos"},
    {'nome': "Kendall Jenner", 'instagram': "@kendalljenner", 'seguidores': 250, 'descrição': "Modelo e empresária", 'país': "Estados Unidos"},
    {'nome': "Justin Bieber", 'instagram': "@justinbieber", 'seguidores': 282, 'descrição': "Cantor canadense", 'país': "Canadá"},
    {'nome': "Neymar Jr.", 'instagram': "@neymarjr", 'seguidores': 180, 'descrição': "Jogador de futebol profissional", 'país': "Brasil"},
    {'nome': "Nicki Minaj", 'instagram': "@nickiminaj", 'seguidores': 150, 'descrição': "Rapper e cantora", 'país': "Trinidad e Tobago"},
    {'nome': "Jennifer Lopez", 'instagram': "@jlo", 'seguidores': 190, 'descrição': "Cantora e atriz", 'país': "Estados Unidos"},
    {'nome': "Virat Kohli", 'instagram': "@virat.kohli", 'seguidores': 250, 'descrição': "Jogador de críquete", 'país': "Índia"},
    {'nome': "Shakira", 'instagram': "@shakira", 'seguidores': 105, 'descrição': "Cantora colombiana", 'país': "Colômbia"},
    {'nome': "Billie Eilish", 'instagram': "@billieeilish", 'seguidores': 120, 'descrição': "Cantora e compositora", 'país': "Estados Unidos"},
    {'nome': "Ellen DeGeneres", 'instagram': "@theellenshow", 'seguidores': 108, 'descrição': "Comediante e apresentadora", 'país': "Estados Unidos"},
    {'nome': "Rihanna", 'instagram': "@badgalriri", 'seguidores': 118, 'descrição': "Cantora e empresária", 'país': "Barbados"},
    {'nome': "David Beckham", 'instagram': "@davidbeckham", 'seguidores': 74, 'descrição': "Ex-jogador de futebol", 'país': "Reino Unido"}
]


def pegar_novo_candidato(excluidos):
    candidatos = [p for p in pessoas if p not in excluidos]
    return random.choice(candidatos) if candidatos else None

def imprimir_pessoa(pessoa, letra):
    print(f"{letra}: {pessoa['nome']}, {pessoa['descrição']}, {pessoa['país']}")


pessoa1 = random.choice(pessoas)
pessoa2 = pegar_novo_candidato([pessoa1])

while pessoa2:
    os.system('cls' if os.name == 'nt' else 'clear')

    imprimir_pessoa(pessoa1, "A")
    imprimir_pessoa(pessoa2, "B")

    escolha = input("Qual deles você acha que tem mais seguidores? (A ou B): ").strip().upper()

    if (pessoa1['seguidores'] > pessoa2['seguidores'] and escolha == 'A') or \
       (pessoa2['seguidores'] > pessoa1['seguidores'] and escolha == 'B'):
        print("Correto!")
    
        if pessoa1['seguidores'] > pessoa2['seguidores']:
            pessoa2 = pegar_novo_candidato([pessoa1, pessoa2])
        else:
            pessoa1 = pessoa2
            pessoa2 = pegar_novo_candidato([pessoa1, pessoa2])
    else:
        print("Você errou!")
        print(f"{pessoa1['nome']} tem {pessoa1['seguidores']} seguidores.")
        print(f"{pessoa2['nome']} tem {pessoa2['seguidores']} seguidores.")
        break
