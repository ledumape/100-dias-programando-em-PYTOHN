from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import os


# Pega a pasta onde o programa está
pasta_programa = os.path.dirname(
    os.path.abspath(__file__)
)

# Caminho do arquivo que guarda as senhas
caminho_dados = os.path.join(
    pasta_programa,
    "dados.json"
)

# Caminho da imagem
caminho_imagem = os.path.join(
    pasta_programa,
    "logo.png"
)


# Gera uma senha aleatória
def gerar_senha():
    letras = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y", "Z"
    ]

    numeros = [
        "0", "1", "2", "3", "4",
        "5", "6", "7", "8", "9"
    ]

    simbolos = [
        "!", "#", "$", "%", "&",
        "(", ")", "*", "+"
    ]

    senha_letras = []

    for _ in range(randint(8, 10)):
        senha_letras.append(choice(letras))

    senha_simbolos = []

    for _ in range(randint(2, 4)):
        senha_simbolos.append(choice(simbolos))

    senha_numeros = []

    for _ in range(randint(2, 4)):
        senha_numeros.append(choice(numeros))

    senha_lista = (
        senha_letras
        + senha_simbolos
        + senha_numeros
    )

    # Mistura os caracteres da senha
    shuffle(senha_lista)

    senha = "".join(senha_lista)

    # Limpa o campo antes de colocar a nova senha
    entrada_senha.delete(0, END)
    entrada_senha.insert(0, senha)

    # Copia a senha para a área de transferência
    janela.clipboard_clear()
    janela.clipboard_append(senha)
    janela.update()

    messagebox.showinfo(
        title="Senha gerada",
        message="A senha foi gerada e copiada."
    )


# Salva os dados no arquivo JSON
def salvar():
    site = entrada_site.get().strip()
    email = entrada_email.get().strip()
    senha = entrada_senha.get().strip()

    novos_dados = {
        site: {
            "email": email,
            "senha": senha
        }
    }

    # Verifica se algum campo está vazio
    if site == "" or email == "" or senha == "":
        messagebox.showinfo(
            title="Campo vazio",
            message="Preencha todos os campos."
        )
        return

    try:
        # Tenta abrir o arquivo existente
        with open(
            caminho_dados,
            mode="r",
            encoding="utf-8"
        ) as arquivo:

            dados = json.load(arquivo)

    except FileNotFoundError:
        # Cria o arquivo se ele não existir
        with open(
            caminho_dados,
            mode="w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                novos_dados,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

    except json.JSONDecodeError:
        # Corrige o arquivo caso ele esteja vazio
        with open(
            caminho_dados,
            mode="w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                novos_dados,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

    else:
        # Adiciona os novos dados
        dados.update(novos_dados)

        with open(
            caminho_dados,
            mode="w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                dados,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

    finally:
        entrada_site.delete(0, END)
        entrada_senha.delete(0, END)
        entrada_site.focus()

    messagebox.showinfo(
        title="Dados salvos",
        message="Os dados foram salvos com sucesso."
    )


# Procura uma senha pelo nome do site
def procurar_senha():
    site = entrada_site.get().strip()

    if site == "":
        messagebox.showinfo(
            title="Campo vazio",
            message="Digite o nome do site."
        )
        return

    try:
        with open(
            caminho_dados,
            mode="r",
            encoding="utf-8"
        ) as arquivo:

            dados = json.load(arquivo)

    except FileNotFoundError:
        messagebox.showinfo(
            title="Erro",
            message="Nenhum arquivo de dados foi encontrado."
        )

    except json.JSONDecodeError:
        messagebox.showinfo(
            title="Erro",
            message="O arquivo de dados está vazio ou danificado."
        )

    else:
        if site in dados:
            email = dados[site]["email"]
            senha = dados[site]["senha"]

            mensagem = (
                f"E-mail ou usuário: {email}\n"
                f"Senha: {senha}"
            )

            messagebox.showinfo(
                title=site,
                message=mensagem
            )

            # Copia a senha encontrada
            janela.clipboard_clear()
            janela.clipboard_append(senha)
            janela.update()

        else:
            messagebox.showinfo(
                title="Não encontrado",
                message=f"Não existem dados salvos para {site}."
            )


# Cria a janela principal
janela = Tk()
janela.title("Gerenciador de Senhas")
janela.config(
    padx=50,
    pady=50
)


# Verifica se a imagem existe
if os.path.exists(caminho_imagem):
    area_imagem = Canvas(
        height=200,
        width=200,
        highlightthickness=0
    )

    imagem_logo = PhotoImage(
        file=caminho_imagem
    )

    area_imagem.create_image(
        100,
        100,
        image=imagem_logo
    )

    area_imagem.grid(
        row=0,
        column=1
    )

else:
    titulo = Label(
        text="Gerenciador de Senhas",
        font=("Arial", 20, "bold")
    )

    titulo.grid(
        row=0,
        column=0,
        columnspan=3,
        pady=40
    )


# Textos dos campos
texto_site = Label(
    text="Site:"
)
texto_site.grid(
    row=1,
    column=0
)

texto_email = Label(
    text="E-mail ou usuário:"
)
texto_email.grid(
    row=2,
    column=0
)

texto_senha = Label(
    text="Senha:"
)
texto_senha.grid(
    row=3,
    column=0
)


# Campo do site
entrada_site = Entry(
    width=21
)
entrada_site.grid(
    row=1,
    column=1
)
entrada_site.focus()


# Campo do e-mail
entrada_email = Entry(
    width=35
)
entrada_email.grid(
    row=2,
    column=1,
    columnspan=2
)

entrada_email.insert(
    0,
    "seuemail@gmail.com"
)


# Campo da senha
entrada_senha = Entry(
    width=21
)
entrada_senha.grid(
    row=3,
    column=1
)


# Botão para procurar uma senha
botao_procurar = Button(
    text="Procurar",
    width=13,
    command=procurar_senha
)
botao_procurar.grid(
    row=1,
    column=2
)


# Botão para gerar uma senha
botao_gerar = Button(
    text="Gerar senha",
    command=gerar_senha
)
botao_gerar.grid(
    row=3,
    column=2
)


# Botão para salvar os dados
botao_salvar = Button(
    text="Salvar",
    width=36,
    command=salvar
)
botao_salvar.grid(
    row=4,
    column=1,
    columnspan=2,
    pady=5
)


# Mantém a janela aberta
janela.mainloop()