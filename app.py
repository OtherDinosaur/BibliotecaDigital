from fastapi import Depends, FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from .routers import router as listaLivros
from .database import get_session
from sqlalchemy.orm import Session
from .models import Livro
from .classes.Relatorio import Relatorio

app = FastAPI(
    title='Biblioteca Digital API',
    description='API para gerenciar livros da biblioteca digital',
    version='0.1.0',
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(listaLivros)

@app.get("/")
def listar_livros(request: Request, session: Session = Depends(get_session)):
    livros = session.query(Livro).all()
    return templates.TemplateResponse("livros.html", {"request": request, "livros": livros})

@app.get("/adicionar-livro")
def adicionar_livro_form(request: Request):
    return templates.TemplateResponse("adicionar_livro.html", {"request": request})

@app.get("/gerar-relatorio")
def gerar_relatorio(request: Request, session: Session = Depends(get_session)):
    livros = session.query(Livro).all()
    relatorio = Relatorio(livros)
    dados_relatorio = {
        "total_livros": relatorio.gerar_rela()["total_livros"],
        "livros_lidos": relatorio.gerar_rela()["livros_lidos"],
        "livros_nao_lidos": relatorio.gerar_rela()["livros_nao_lidos"],
        "percentual": relatorio.gerar_percen(),
        "media_tempo": relatorio.gerar_media(),
        "genero_fav": relatorio.genero_fav(),
        "top5": relatorio.gerar_top5(),
        "livros": relatorio.gerar_rela()["livros"]
    }
    return templates.TemplateResponse("relatorio.html", {"request": request, "relatorio": dados_relatorio})
@app.get("/livros/deletar/{livro_id}")
def confirmar_delecao(request: Request, livro_id: int, session: Session = Depends(get_session)):
    livro = session.get(Livro, livro_id)
    if not livro:
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse("deletar_livro.html", {"request": request, "livro": livro})

@app.post("/livros/deletar/{livro_id}")
def deletar_livro(livro_id: int, id: int = Form(...), session: Session = Depends(get_session)):
    livro = session.get(Livro, livro_id)
    if livro:
        session.delete(livro)
        session.commit()
    return RedirectResponse(url="/", status_code=303)

@app.get("/livros/editar/{livro_id}")
def editar_livro_form(request: Request, livro_id: int, session: Session = Depends(get_session)):
    livro = session.get(Livro, livro_id)
    if not livro:
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse("editar_livro.html", {"request": request, "livro": livro})

@app.post("/livros/editar/{livro_id}")
def atualizar_livro(
    livro_id: int,
    titulo: str = Form(...),
    autor: str = Form(...),
    ano: int = Form(...),
    genero: str = Form(...),
    data_in: str = Form(...),
    data_ter: str = Form(None),
    session: Session = Depends(get_session)
):
    livro = session.get(Livro, livro_id)
    if not livro:
        return RedirectResponse(url="/", status_code=303)
    
    # Atualiza os campos
    livro.titulo = titulo
    livro.autor = autor
    livro.ano = ano
    livro.genero = genero
    livro.data_in = data_in
    livro.data_ter = data_ter
    # Calcula o status: True (Lido) se data_ter foi preenchida, False (Não Lido) caso contrário
    livro.status = bool(data_ter and data_ter.strip())
    
    session.commit()
    return RedirectResponse(url="/", status_code=303)
