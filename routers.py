from fastapi import APIRouter, Depends, status, HTTPException, Form, Request
from .schemas import LivroSchema, LivroPub, LivroList, LivroUpdate
from .database import get_session
from sqlalchemy import select
from sqlalchemy.orm import Session
from .models import Livro
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

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

@router.get('/livros', response_model=LivroList, status_code=status.HTTP_200_OK)
def listaLivros(session: Session = Depends(get_session), offset: int = 0, limit: int = 50):
   query = session.scalars(select(Livro).offset(offset).limit(limit))
   livros = query.all()
   return { 'livros': livros }

@router.get('/{livro_id}', response_model=LivroPub, status_code=status.HTTP_200_OK)
def mostraLivro(livro_id: int, session: Session = Depends(get_session)):
   livro = session.get(Livro, livro_id)
   if not livro:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Livro não encontrado')
   return livro

@router.delete('/delete/{livro_id}', status_code=status.HTTP_204_NO_CONTENT)
def deletar_livro(livro_id: int, session: Session = Depends(get_session)):
    livro = session.get(Livro, livro_id)
    if livro:
        session.delete(livro)
        session.commit()
    return RedirectResponse(url="/", status_code=303)

@router.put('/{livro_id}', response_model=LivroPub, status_code=status.HTTP_201_CREATED)
def atualizaLivro(livro_id: int, livro_at: LivroSchema, session: Session = Depends(get_session)):
   livro = session.get(Livro, livro_id)
   if not livro:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Livro não encontrado')
   for key, value in livro_at.model_dump().items():
      setattr(livro, key, value)
   session.commit()
   session.refresh(livro)
   return livro

@router.patch('/{livro_id}/status', response_model=LivroPub, status_code=status.HTTP_200_OK)
def atualizaStatusLivro(livro_id: int, livro_at: LivroUpdate, session: Session = Depends(get_session)):
   livro = session.get(Livro, livro_id)
   if not livro:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Livro não encontrado')
   for key, value in livro_at.model_dump(exclude_unset=True).items():
      setattr(livro, key, value)
   session.commit()
   session.refresh(livro)
   return livro

@router.post('/form', response_model=LivroPub, status_code=status.HTTP_201_CREATED)
def criaLivrosForm(
    titulo: str = Form(...),
    autor: str = Form(...),
    ano: int = Form(...),
    genero: str = Form(...),
    data_in: str = Form(...),
    data_ter: str = Form(None),
    status: bool = Form(...),
    session: Session = Depends(get_session)
):
    livro = Livro(titulo=titulo, autor=autor, ano=ano, genero=genero, data_in=data_in, data_ter=data_ter, status=status)
    session.add(livro)
    session.commit()
    session.refresh(livro)
    return RedirectResponse(url="/", status_code=303)