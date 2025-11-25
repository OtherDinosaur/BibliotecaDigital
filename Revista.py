class Livro:
    """
    Classe para armazenar as revistas e suas características
    """
    def __init__(self,titulo,ano,autor,genero,num_paginas,status):
        self.__titulo = titulo
        self.__ano = ano
        self.__autor = autor
        self.genero = genero
        self.num_paginas = num_paginas
        self.status = status

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def autor(self):
        return self.__autor
    
    

    def alterar_status(self,status):
        self.status = status

    def CRUD(self,comando):
        pass