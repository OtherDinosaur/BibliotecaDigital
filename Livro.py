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
        self.status = status

    def CRUD(self,comando):
        if comando == criar:
            
