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