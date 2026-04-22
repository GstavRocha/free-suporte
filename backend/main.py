from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlmodel import Session

from core.db import get_session

app = FastAPI()

@app.get("/")
async def test():
    return {"message": "Hello World"}

@app.get("/health/db")
def database_health(session: Session = Depends(get_session)):
    session.exec(text("SELECT 1"))
    return {"database": "connected"}
