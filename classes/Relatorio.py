from datetime import datetime
from collections import Counter

class Relatorio:
  """
  Classe para gerar os relatórios e suas características
  """
  def __init__(self, livros):
      self.__livros = livros

  @property
  def livros(self):
    return self.__livros

  def gerar_rela(self):
      """Gera relatório geral com todos os livros"""
      return {
          "total_livros": len(self.__livros),
          "livros_lidos": len([l for l in self.__livros if l.status]),
          "livros_nao_lidos": len([l for l in self.__livros if not l.status]),
          "livros": [{"titulo": l.titulo, "autor": l.autor, "ano": l.ano, "genero": l.genero, "status": l.status} for l in self.__livros]
      }

  def gerar_percen(self):
      """Gera percentual de livros lidos"""
      if not self.__livros:
          return 0.0
      lidos = len([l for l in self.__livros if l.status])
      return round((lidos / len(self.__livros)) * 100, 2)

  def gerar_media(self):
      """Gera média de tempo de leitura em dias"""
      tempos = []
      for l in self.__livros:
          if l.status and l.data_in and l.data_ter:
              try:
                  data_in = datetime.strptime(l.data_in, "%Y-%m-%d")
                  data_ter = datetime.strptime(l.data_ter, "%Y-%m-%d")
                  tempo = (data_ter - data_in).days
                  if tempo > 0:  # Só conta tempos positivos
                      tempos.append(tempo)
              except (ValueError, TypeError):
                  continue
      if not tempos:
          return 0.0
      return round(sum(tempos) / len(tempos), 1)

  def gerar_top5(self):
      """Gera top 5 livros por ano (mais recentes)"""
      livros_ordenados = sorted(self.__livros, key=lambda l: l.ano, reverse=True)
      return [{"titulo": l.titulo, "autor": l.autor, "ano": l.ano} for l in livros_ordenados[:5]]

  def genero_fav(self):
      """Gera gênero favorito (mais frequente)"""
      generos = [l.genero for l in self.__livros if l.genero]
      if not generos:
          return "Nenhum"
      contador = Counter(generos)
      return contador.most_common(1)[0][0]