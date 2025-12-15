from pydantic import BaseModel
from typing import Optional

class LivroSchema(BaseModel):
    titulo: str 
    autor: str
    ano: int
    genero: str
    data_in: int
    data_ter: Optional[int] = None
    status: bool

class LivroPub(BaseModel):
    id: int
    titulo: str 
    autor: str
    ano: int
    genero: str
    data_in: int
    data_ter: Optional[int] = None
    status: bool

class LivroUpdate(BaseModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    ano: Optional[int] = None
    genero: Optional[str] = None
    data_in: Optional[int] = None
    data_ter: Optional[int] = None
    status: Optional[bool] = None

class LivroList(BaseModel):
    livros: list[LivroPub] 