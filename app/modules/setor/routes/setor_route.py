from fastapi import APIRouter

router = APIRouter()
@router.get("/")
def list_setor():
    return {"msg": "setor funcionando"}