class Livro
    def __init__(self,titulo,ano,autor,tipo,genero,num_paginas,status)
        self.titulo = 
        self.ano = 
        self.autor = 
        self.tipo = 
        self.genero = 
        self.num_paginas = 
        self.status = 

    def alterar_status(self,status)

    def CRUD(self,comando)

class Anotacao
    def __init__(self,texto,data,trecho,livro)
        self.texto = 
        self.data = 
        self.trecho = 
        self.livro = 

    def criar_nota(self,livro,texto)

class Relatorio
    def __init__(self,Livro)
        self.Livro = livro

    def gerar_rela(self)

    def gerar_percen(self)

    def gerar_media(self)

    def gerar_top5(self)

    def genero_fav(self)

class Filtro
    def __init__(self,Livro)
        self.Livro = livro
    
    def filtrar(self)