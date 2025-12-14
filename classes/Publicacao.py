class Publicacao:
    """
    Classe para armazenar publicações e suas características
    """
    def __init__(self,titulo,ano,autor,genero,num_paginas,data_in,data_ter,status):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
        self.genero = genero
        self.num_paginas = num_paginas
        self.data_in = data_in
        self.data_ter = data_ter
        self.status = status

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self,titulo):
        self.__titulo = titulo
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self,ano):
        try:
            ano = int(ano)
            self.__ano = ano 
        except ValueError:
            raise ValueError("O ano deve ser um número inteiro.")
            
    
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self,autor):
        self.__autor = autor
    
    

    def alterar_status(self,status):
        self.status = status

    def CRUD(self,comando):
        pass