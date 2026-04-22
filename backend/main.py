from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlmodel import Session

from core.db import get_session
from backend.modules.usuario.routes.usuario_route import  router as usuario_router
from backend.modules.log.routes.log_route import router as log_router
from backend.modules.anexo.routes.anexo_route import router as anexo_route
from backend.modules.


# @app.get("/")
# async def test():
#     return {"message": "Hello World"}
#
# @app.get("/health/db")
# def database_health(session: Session = Depends(get_session)):
#     session.exec(text("SELECT 1"))
#     return {"database": "connected"}
