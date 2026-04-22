from fastapi import APIRouter

router = APIRouter()
@router.get("/")
def list_log():
    return {"msg": "log funcionando"}