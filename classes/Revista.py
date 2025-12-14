from Publicacao import Publicacao


class Revista(Publicacao):
    """
    Classe para armazenar as revistas e suas características
    """
    def __init__(self,titulo,ano,autor,genero,num_paginas,status):
        super().__init__(titulo,ano,autor,genero,num_paginas,status)