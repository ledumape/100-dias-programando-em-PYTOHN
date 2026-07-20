
from tkinter import *

# Cria a janela principal
janela = Tk()
janela.title("Exemplos de Widgets")
janela.minsize(width=600, height=650)
janela.config(padx=30, pady=30)


# Função chamada quando o botão principal é clicado
def botao_clicado():
    texto_digitado = entrada.get()

    if texto_digitado == "":
        rotulo.config(text="Digite alguma coisa.")
    else:
        rotulo.config(text=texto_digitado)


# Mostra o valor escolhido no Spinbox
def spinbox_usado():
    valor = spinbox.get()
    print(f"Valor do Spinbox: {valor}")


# Mostra o valor atual da escala
def escala_usada(valor):
    print(f"Valor da escala: {valor}")


# Mostra se a caixa está marcada
def caixa_marcada():
    valor = estado_caixa.get()

    if valor == 1:
        print("A caixa está marcada.")
    else:
        print("A caixa está desmarcada.")


# Mostra a opção escolhida
def opcao_escolhida():
    valor = estado_opcao.get()

    if valor == 1:
        print("Você escolheu a opção 1.")
    elif valor == 2:
        print("Você escolheu a opção 2.")


# Mostra o item escolhido na lista
def item_selecionado(evento):
    selecao = lista.curselection()

    if selecao:
        item = lista.get(selecao)
        print(f"Item escolhido: {item}")


# Título da janela
titulo = Label(
    text="Exemplos de Tkinter",
    font=("Arial", 22, "bold")
)
titulo.grid(column=0, row=0, columnspan=2, pady=15)


# Rótulo que terá o texto alterado
rotulo = Label(
    text="Digite um texto abaixo",
    font=("Arial", 14, "normal")
)
rotulo.grid(column=0, row=1, columnspan=2, pady=10)


# Campo para digitar texto
entrada = Entry(width=30)
entrada.insert(END, "Texto inicial")
entrada.grid(column=0, row=2, padx=10, pady=10)


# Botão que altera o rótulo
botao = Button(
    text="Alterar texto",
    command=botao_clicado
)
botao.grid(column=1, row=2, padx=10, pady=10)


# Caixa de texto com várias linhas
caixa_texto = Text(height=5, width=40)
caixa_texto.insert(
    END,
    "Este é um exemplo de uma caixa de texto com várias linhas."
)
caixa_texto.grid(column=0, row=3, columnspan=2, pady=15)


# Spinbox para escolher um número
texto_spinbox = Label(text="Escolha um número:")
texto_spinbox.grid(column=0, row=4, pady=5)

spinbox = Spinbox(
    from_=0,
    to=10,
    width=10,
    command=spinbox_usado
)
spinbox.grid(column=1, row=4, pady=5)


# Escala de 0 até 100
texto_escala = Label(text="Escolha um valor:")
texto_escala.grid(column=0, row=5, pady=5)

escala = Scale(
    from_=0,
    to=100,
    orient="horizontal",
    command=escala_usada
)
escala.grid(column=1, row=5, pady=5)


# Variável que guarda o estado da caixa
estado_caixa = IntVar()

caixa_selecao = Checkbutton(
    text="Ativar opção",
    variable=estado_caixa,
    command=caixa_marcada
)
caixa_selecao.grid(column=0, row=6, columnspan=2, pady=10)


# Variável que guarda a opção marcada
estado_opcao = IntVar()

opcao1 = Radiobutton(
    text="Opção 1",
    value=1,
    variable=estado_opcao,
    command=opcao_escolhida
)

opcao2 = Radiobutton(
    text="Opção 2",
    value=2,
    variable=estado_opcao,
    command=opcao_escolhida
)

opcao1.grid(column=0, row=7, pady=5)
opcao2.grid(column=1, row=7, pady=5)


# Lista de frutas
frutas = [
    "Maçã",
    "Pera",
    "Laranja",
    "Banana"
]

lista = Listbox(height=4)

for fruta in frutas:
    lista.insert(END, fruta)

lista.bind(
    "<<ListboxSelect>>",
    item_selecionado
)

lista.grid(column=0, row=8, columnspan=2, pady=15)


# Mantém a janela aberta
janela.mainloop()

