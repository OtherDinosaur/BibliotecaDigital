from fastapi import FastAPI
from .routers import router as listaLivros

app = FastAPI(
    title='Fast Car API',
    description='PycodeBR modern Car API',
    version='0.1.0',
)

app.include_router(listaLivros)

@app.get('/')
def read_root():
    return {'status': 'ok'}