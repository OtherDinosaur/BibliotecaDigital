from Livro import Livro
import json
from datetime import date
import tkinter as tk
from tkinter import ttk



"""
window = tk.Tk()
window.title("Biblioteca Digital")
window.geometry("400x300")
label = ttk.Label(window, text="Bom dia, bem vindo ao menu da Biblioteca Digital mágica")
label.pack(pady=20)
button = ttk.Button(window, text="Clique aqui para começar")
button.pack(pady=10)

frame

window.mainloop()  
"""

print("Bom dia")

print("bem vindo ao menu da Biblioteca Digital mágica: selecione uma das funções para começar:" \
"1 - Editar Livros" \
"2 - Editar Revistas" \
"3 - Fazer anotação" \
"4 - Dar nota a um livro" \
"5 - Alterar Status de leitura" \
"6 - Buscar Filtros" \
"7 - Visualizar relatórios")
opcao = int(input())

if opcao == 1:
    print("Agora selecione uma das funções de livros:" \
    "1 - adicionar livro" \
    "2 - remover livro" \
    "3 - visualizar livro" \
    "4 - alterar informações de livro")
    opcao1 = int(input())
    if opcao1 == 1:
        titulo = input("1Digite o título da obra: ")
        autor = input("Digite o autor da obra: ")
        ano = input("Digite o ano da publicação")
        genero = input("Digite o gênero da obra")
        data_in = date.today()
        if input("Digitar data de conclusão? Y/N") == "Y":
            data_ter = input("Digite a data de conclusão: ")
        else:
            data_ter = None
        num_paginas = int(input("digite o número de páginas do livro"))
        if data_ter == None:
            status = False
        else:
            status = True
        livro = Livro(titulo,ano,autor,genero,num_paginas,status)

        with open('Livros.json', 'w', encoding='utf-8') as f:
            json.dump(livro.__dict__, f, ensure_ascii=False, indent=4)