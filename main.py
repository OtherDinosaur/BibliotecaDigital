class Livro:
    """
    Classe para armazenar os livros e suas características
    """
    def __init__(self,titulo,ano,autor,tipo,genero,num_paginas,status):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
        self.tipo = tipo
        self.genero = genero
        self.num_paginas = num_paginas
        self.status = status

    def alterar_status(self,status):

    def CRUD(self,comando):

class Anotacao:
     """
    Classe para criar as anotações dos livros e suas características
    """
    def __init__(self,texto,data,trecho,livro):
        self.texto = texto
        self.data = data
        self.trecho = trecho
        self.livro = livro

    def criar_nota(self,livro,texto):

class Relatorio:
     """
    Classe para gerar os relatórios e suas características
    """
    def __init__(self,livro):
        self.livro = livro

    def gerar_rela(self):

    def gerar_percen(self):

    def gerar_media(self):

    def gerar_top5(self):

    def genero_fav(self):

class Filtro:
     """
    Classe para armazenar os filtros a serem criados e suas características
    """
    def __init__(self,livro):
        self.livro = livro
    
    def filtrar(self):
      pass
