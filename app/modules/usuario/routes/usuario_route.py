from fastapi import  APIRouter

router = APIRouter()

@router.get("/")
def list_usuarios():
    return {"msg": "usuarios funcionando"}