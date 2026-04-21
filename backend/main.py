# preciso ao menos importar para a main para conseguir depurar
from fastapi import FastAPI

from config.dbconnect import database_url

app = FastAPI()

@app.get("/")
async def test():
    return {"message": "Hello World"}

# @app.get("/health/db")
# async def database_health():
#     return {"database": "connected" if check_connection() else "disconnected"}

