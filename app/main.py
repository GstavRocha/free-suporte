from fastapi import Depends, FastAPI
from pycodestyle import register_check
from sqlalchemy import text
from sqlmodel import Session

from core.db import get_session
# from app.modules.usuario.routes.usuario_route import  router as usuario_router
# from app.modules.log.routes.log_route import router as log_router
# from app.modules.anexo.routes.anexo_route import router as anexo_route
# from app.modules.chamado.routes.chamado_router import router as chamado_router
# from app.modules.comentario.routes.comenterio_route import router as comentario_router
# from app.modules.setor.routes.setor_route import router as setor_router

from app.modules.anexo.routes.anexo_route import router
# def register_healthcheck(app: FastAPI):
#     @app.get("/health", tags=["Health"])
#     def health_check():
#         return {"status": "ok"}
# def register_routers(app: FastAPI):
#     API_PREFIX = "/api/v1"
#     app.include_router(usuario_router, prefix=f"{API_PREFIX}/usuarios", tags=["Usuarios"])
#     app.include_router(log_router, prefix=f"{API_PREFIX}/log", tags=["Logs"])
#     app.include_router(anexo_route, prefix=f"{API_PREFIX}/anexo", tags=["Anexos"])
#     app.include_router(chamado_router,prefix=f"{API_PREFIX}/chamado", tags=["Chamados"])
#     app.include_router(comentario_router,prefix=f"{API_PREFIX}/comentarios", tags=["Comentários"])
#     app.include_router(setor_router, prefix=f"{API_PREFIX}/setor", tags=["Setor"])

app = FastAPI(
    title="Suporte Flow API",
    version="1.0.0"
)