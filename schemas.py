from pydantic import BaseModel
from typing import Optional

class LivroSchema(BaseModel):
    titulo: str 
    autor: str
    ano: int
    genero: str
    data_in: str
    data_ter: Optional[str] = None
    status: bool

class LivroPub(BaseModel):
    id: int
    titulo: str 
    autor: str
    ano: int
    genero: str
    data_in: str
    data_ter: Optional[str] = None
    status: bool

class LivroUpdate(BaseModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    ano: Optional[int] = None
    genero: Optional[str] = None
    data_in: Optional[str] = None
    data_ter: Optional[str] = None
    status: Optional[bool] = None

class LivroList(BaseModel):
    livros: list[LivroPub] 