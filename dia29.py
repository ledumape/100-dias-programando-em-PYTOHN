
from tkinter import *
from tkinter import messagebox
import random
import os

# Listas usadas para criar as senhas
LETRAS = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z"
]

NUMEROS = [
    "0", "1", "2", "3", "4",
    "5", "6", "7", "8", "9"
]

SIMBOLOS = [
    "!", "#", "$", "%", "&",
    "(", ")", "*", "+"
]

# Pega a pasta onde o arquivo Python está
pasta_programa = os.path.dirname(
    os.path.abspath(__file__)
)

# Define onde o arquivo de senhas será salvo
caminho_arquivo = os.path.join(
    pasta_programa,
    "senhas.txt"
)


# Gera uma senha aleatória
def gerar_senha():
    senha = []

    quantidade_letras = random.randint(8, 10)
    quantidade_simbolos = random.randint(2, 4)
    quantidade_numeros = random.randint(2, 4)

    # Adiciona letras
    for _ in range(quantidade_letras):
        senha.append(random.choice(LETRAS))

    # Adiciona símbolos
    for _ in range(quantidade_simbolos):
        senha.append(random.choice(SIMBOLOS))

    # Adiciona números
    for _ in range(quantidade_numeros):
        senha.append(random.choice(NUMEROS))

    # Mistura os caracteres
    random.shuffle(senha)

    senha_final = "".join(senha)

    # Coloca a senha no campo
    entrada_senha.delete(0, END)
    entrada_senha.insert(0, senha_final)

    # Copia a senha
    janela.clipboard_clear()
    janela.clipboard_append(senha_final)

    mensagem_status.config(
        text="Senha gerada e copiada.",
        fg="green"
    )


# Salva os dados no arquivo
def salvar_senha():
    site = entrada_site.get().strip()
    email = entrada_email.get().strip()
    senha = entrada_senha.get().strip()

    # Verifica se há campos vazios
    if site == "" or email == "" or senha == "":
        messagebox.showinfo(
            title="Campo vazio",
            message="Preencha todos os campos."
        )
        return

    confirmacao = messagebox.askokcancel(
        title=site,
        message=(
            f"Site: {site}\n"
            f"E-mail ou usuário: {email}\n"
            f"Senha: {senha}\n\n"
            "Deseja salvar esses dados?"
        )
    )

    if confirmacao:
        with open(
            caminho_arquivo,
            mode="a",
            encoding="utf-8"
        ) as arquivo:

            arquivo.write(
                f"Site: {site} | "
                f"E-mail: {email} | "
                f"Senha: {senha}\n"
            )

        # Limpa os campos depois de salvar
        entrada_site.delete(0, END)
        entrada_senha.delete(0, END)
        entrada_site.focus()

        mensagem_status.config(
            text="Senha salva com sucesso.",
            fg="green"
        )


# Mostra o local onde o arquivo foi salvo
def mostrar_local_arquivo():
    messagebox.showinfo(
        title="Local do arquivo",
        message=f"As senhas estão salvas em:\n\n{caminho_arquivo}"
    )


# Cria a janela
janela = Tk()
janela.title("Gerenciador de Senhas")
janela.config(
    padx=50,
    pady=40
)

# Título do programa
titulo = Label(
    text="Gerenciador de Senhas",
    font=("Arial", 22, "bold")
)
titulo.grid(
    row=0,
    column=0,
    columnspan=3,
    pady=(0, 25)
)

# Textos dos campos
texto_site = Label(text="Site:")
texto_site.grid(
    row=1,
    column=0,
    sticky="e"
)

texto_email = Label(text="E-mail ou usuário:")
texto_email.grid(
    row=2,
    column=0,
    sticky="e"
)

texto_senha = Label(text="Senha:")
texto_senha.grid(
    row=3,
    column=0,
    sticky="e"
)

# Campo do site
entrada_site = Entry(width=38)
entrada_site.grid(
    row=1,
    column=1,
    columnspan=2,
    pady=3
)
entrada_site.focus()

# Campo do e-mail
entrada_email = Entry(width=38)
entrada_email.grid(
    row=2,
    column=1,
    columnspan=2,
    pady=3
)
entrada_email.insert(
    0,
    "seuemail@gmail.com"
)

# Campo da senha
entrada_senha = Entry(width=22)
entrada_senha.grid(
    row=3,
    column=1,
    pady=3
)

# Botão para gerar senha
botao_gerar = Button(
    text="Gerar senha",
    command=gerar_senha
)
botao_gerar.grid(
    row=3,
    column=2,
    padx=3
)

# Botão para salvar
botao_salvar = Button(
    text="Salvar",
    width=32,
    command=salvar_senha
)
botao_salvar.grid(
    row=4,
    column=1,
    columnspan=2,
    pady=8
)

# Botão para mostrar o local do arquivo
botao_local = Button(
    text="Mostrar local do arquivo",
    width=32,
    command=mostrar_local_arquivo
)
botao_local.grid(
    row=5,
    column=1,
    columnspan=2
)

# Mensagem de resultado
mensagem_status = Label(
    text="",
    font=("Arial", 10)
)
mensagem_status.grid(
    row=6,
    column=0,
    columnspan=3,
    pady=10
)

# Mantém a janela aberta
janela.mainloop()