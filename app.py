from fastapi import Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .routers import router as listaLivros
from .database import get_session
from sqlalchemy.orm import Session
from .models import Livro

app = FastAPI(
    title='Biblioteca Digital API',
    description='API para gerenciar livros da biblioteca digital',
    version='0.1.0',
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(listaLivros)

@app.get('/')
def read_root():
    return {'status': 'ok'}

@app.get("/livros")
def listar_livros(request: Request, session: Session = Depends(get_session)):
    livros = session.query(Livro).all()
    return templates.TemplateResponse("livros.html", {"request": request, "livros": livros})

@app.get("/adicionar-livro")
def adicionar_livro_form(request: Request):
    return templates.TemplateResponse("adicionar_livro.html", {"request": request})