import Publicacao


class Livro(Publicacao):
    """
    Classe para armazenar os livros e suas características
    """
    def __init__(self,titulo,ano,autor,genero,num_paginas,status):
        super().__init__(self,titulo,ano,autor,genero,num_paginas,status)