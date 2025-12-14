from fastapi import APIRouter, Depends, status
from .schemas import LivroSchema, LivroPub
from .database import get_session
from sqlalchemy.orm import Session
from .models import Livro

router = APIRouter(
    prefix='/api/Biblioteca',
    tags=['Biblioteca'],
)

@router.post('/', response_model=LivroPub, status_code=status.HTTP_201_CREATED)
def criaLivros(livro:LivroSchema, session: Session = Depends(get_session)):
   livro = Livro(**livro.model_dump())
   session.add(livro)
   session.commit()
   session.refresh(livro)
   return livro