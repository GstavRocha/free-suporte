from fastapi import APIRouter

router = APIRouter()
@router.get("/")
def list_chamado():
    return {"msg": "chamado funcionando"}