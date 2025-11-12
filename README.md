# BibliotecaDigital
Código de uma biblioteca digital para a disciplina de POO

O aplicativo consistirá em uma Biblioteca digital para controle de leitura do usuário, com o registro dos livros e todas as informações, status de leitura, algumas anotações e avaliações do próprio usuário. O sistema é capaz de resgatar essas informações e gerar filtros e relatórios.

Classes: 

_____________________________________________
Livro 

titulo: str
ano: int
autor: str
tipo: boolean
genero: str
num_paginas: int
status: boolean

CRUD()
alterar_status()
data_inicio()
data_termino()

_____________________________________________
Relatorio

Livro: objeto

gerar_rela()
gerar_percen()
gerar_media()
gerar_top5()
genero_fav()

_____________________________________________
Anotacao

texto: str
data: int
trecho: str
Livro: objeto

criar_nota()
listar_nota()

_____________________________________________
Filtro

Livro: objeto

filtrar()