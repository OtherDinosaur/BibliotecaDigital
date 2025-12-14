from sqlalchemy import Column, Integer, String, Boolean
from datetime import date
from .database import Base


class Livro(Base):
    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    genero = Column(String, nullable=False)
    data_in = Column(Integer, nullable=False)
    data_ter = Column(Integer, nullable=True)
    status = Column(Boolean, nullable=False)