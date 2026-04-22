from fastapi import APIRouter

router = APIRouter()
@router.get("/")
def list_anexo():
    return {"msg": "anexos funcionando"}
