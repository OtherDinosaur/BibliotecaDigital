from fastapi import APIRouter, status
from sqlalchemy import Session

router = APIRouter(
    prefix='/api/v1/Bilbioteca',
    tags=['Biblioteca'],
)

@router.get('/')
def listaLivros():
    return {
        'cars': [
            {'id': 1, 'modelo': 'Marea 20v'},
            {'id': 2, 'modelo': 'Opala'},
            {'id': 3, 'modelo': 'Corsa Wind'},
        ]
    }