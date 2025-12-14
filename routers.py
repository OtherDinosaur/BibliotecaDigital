from fastapi import APIRouter, Depends, status, HTTPException
from .schemas import LivroSchema, LivroPub, LivroList
from .database import get_session
from sqlalchemy import select
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

@router.get('/', response_model=LivroList, status_code=status.HTTP_200_OK)
def listaLivros(session: Session = Depends(get_session), offset: int = 0, limit: int = 50):
   query = session.scalars(select(Livro).offset(offset).limit(limit))
   livros = query.all()
   return { 'livros': livros }

@router.get('/{livro_id}', response_model=LivroPub, status_code=status.HTTP_200_OK)
def mostraLivro(livro_id: int, session: Session = Depends(get_session)):
   livro = session.get(Livro, livro_id)
   if not livro:

      return { 'erro': 'Livro não encontrado' }
   return livro