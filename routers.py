from fastapi import APIRouter, status

router = APIRouter(
    prefix='/api/Bilbioteca',
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