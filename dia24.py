import os

# Nome que será substituído na carta
MARCADOR_NOME = "[nome]"

# Lista de pessoas convidadas
nomes_convidados = [
    "Aang",
    "Zuko",
    "Appa",
    "Katara",
    "Sokka",
    "Momo",
    "Tio Iroh",
    "Toph"
]

# Modelo usado para criar todas as cartas
modelo_carta = """Olá, [nome],

Você está convidado para a minha festa de aniversário neste sábado.

Espero que você possa comparecer!

Angela
"""

# Nome da pasta onde as cartas serão salvas
pasta_cartas = "Cartas prontas"

# Cria a pasta caso ela ainda não exista
if not os.path.exists(pasta_cartas):
    os.mkdir(pasta_cartas)

# Cria uma carta para cada pessoa da lista
for nome in nomes_convidados:

    nova_carta = modelo_carta.replace(
        MARCADOR_NOME,
        nome
    )

    nome_arquivo = f"carta_para_{nome}.txt"
    caminho_arquivo = os.path.join(
        pasta_cartas,
        nome_arquivo
    )

    # Salva a carta em um arquivo de texto
    with open(
        caminho_arquivo,
        mode="w",
        encoding="utf-8"
    ) as arquivo_carta:

        arquivo_carta.write(nova_carta)

    print(f"Carta criada para {nome}.")

print("\nTodas as cartas foram criadas!")