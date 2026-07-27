import requests
from datetime import datetime


# Dados da sua conta no Pixela
NOME_USUARIO = "SEU_NOME_DE_USUARIO"
TOKEN = "SEU_TOKEN"
ID_GRAFICO = "grafico1"

# Endereço principal da API
ENDERECO_PIXELA = "https://pixe.la/v1/users"

# Cabeçalho usado para confirmar sua identidade
cabecalho = {
    "X-USER-TOKEN": TOKEN
}


# Cria uma conta no Pixela
def criar_usuario():
    dados_usuario = {
        "token": TOKEN,
        "username": NOME_USUARIO,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    try:
        resposta = requests.post(
            url=ENDERECO_PIXELA,
            json=dados_usuario,
            timeout=10
        )

        print(resposta.text)

    except requests.RequestException as erro:
        print("Não foi possível criar o usuário.")
        print(erro)


# Cria um gráfico para registrar o hábito
def criar_grafico():
    endereco_grafico = (
        f"{ENDERECO_PIXELA}/"
        f"{NOME_USUARIO}/graphs"
    )

    configuracao_grafico = {
        "id": ID_GRAFICO,
        "name": "Gráfico de ciclismo",
        "unit": "Km",
        "type": "float",
        "color": "ajisai"
    }

    try:
        resposta = requests.post(
            url=endereco_grafico,
            json=configuracao_grafico,
            headers=cabecalho,
            timeout=10
        )

        print(resposta.text)

    except requests.RequestException as erro:
        print("Não foi possível criar o gráfico.")
        print(erro)


# Registra a quantidade feita hoje
def registrar_habito():
    hoje = datetime.now()

    quantidade = input(
        "Quantos quilômetros você pedalou hoje? "
    )

    endereco_registro = (
        f"{ENDERECO_PIXELA}/"
        f"{NOME_USUARIO}/graphs/"
        f"{ID_GRAFICO}"
    )

    dados_registro = {
        "date": hoje.strftime("%Y%m%d"),
        "quantity": quantidade
    }

    try:
        resposta = requests.post(
            url=endereco_registro,
            json=dados_registro,
            headers=cabecalho,
            timeout=10
        )

        print(resposta.text)

    except requests.RequestException as erro:
        print("Não foi possível registrar o hábito.")
        print(erro)


# Altera o registro de uma data
def atualizar_habito():
    data = input(
        "Digite a data que deseja alterar no formato AAAAMMDD: "
    )

    nova_quantidade = input(
        "Digite a nova quantidade: "
    )

    endereco_atualizacao = (
        f"{ENDERECO_PIXELA}/"
        f"{NOME_USUARIO}/graphs/"
        f"{ID_GRAFICO}/{data}"
    )

    novos_dados = {
        "quantity": nova_quantidade
    }

    try:
        resposta = requests.put(
            url=endereco_atualizacao,
            json=novos_dados,
            headers=cabecalho,
            timeout=10
        )

        print(resposta.text)

    except requests.RequestException as erro:
        print("Não foi possível atualizar o hábito.")
        print(erro)


# Exclui o registro de uma data
def excluir_habito():
    data = input(
        "Digite a data que deseja excluir no formato AAAAMMDD: "
    )

    endereco_exclusao = (
        f"{ENDERECO_PIXELA}/"
        f"{NOME_USUARIO}/graphs/"
        f"{ID_GRAFICO}/{data}"
    )

    try:
        resposta = requests.delete(
            url=endereco_exclusao,
            headers=cabecalho,
            timeout=10
        )

        print(resposta.text)

    except requests.RequestException as erro:
        print("Não foi possível excluir o hábito.")
        print(erro)


# Mostra as opções do programa
def mostrar_menu():
    print()
    print("CONTROLE DE HÁBITOS")
    print()
    print("1 - Criar usuário")
    print("2 - Criar gráfico")
    print("3 - Registrar hábito de hoje")
    print("4 - Atualizar um registro")
    print("5 - Excluir um registro")
    print("6 - Sair")
    print()


# Mantém o programa funcionando
while True:
    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_usuario()

    elif opcao == "2":
        criar_grafico()

    elif opcao == "3":
        registrar_habito()

    elif opcao == "4":
        atualizar_habito()

    elif opcao == "5":
        excluir_habito()

    elif opcao == "6":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")