class Anotacao:
     """
    Classe para criar as anotações dos livros e suas características
    """
    def __init__(self,texto,data,trecho,livro):
        self._texto = texto
        self.__data = data
        self.trecho = trecho
        self.__livro = livro

    @property
    def data(self):
        return self.__data

    @property
    def livro(self):
        return self.__livro

    def criar_nota(self,livro,texto):
       pass