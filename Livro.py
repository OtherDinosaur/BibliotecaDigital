from classes.Publicacao import Publicacao


class Livro(Publicacao):
    """
    Classe para armazenar os livros e suas características
    """
    def __init__(self,titulo,ano,autor,genero,num_paginas,data_in,data_ter,status):
        super().__init__(titulo,ano,autor,genero,num_paginas,data_in,data_ter,status)