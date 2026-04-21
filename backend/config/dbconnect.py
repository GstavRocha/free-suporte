from collections.abc import Generator
from pathlib import Path
import os

from dotenv import load_dotenv
from sqlalchemy import text
from sqlalchemy.engine import URL
from sqlmodel import Session, create_engine


BASE_DIR = Path(__file__).resolve().parents[1]

# for env_path in (
#     BASE_DIR / ".env",
#     BASE_DIR / "backend" / ".env",
#     BASE_DIR / "docker" / ".env",
# ):
    # load_dotenv(BASE_DIR/".env", override=False)
env_path = f'{BASE_DIR}/.env'
load = load_dotenv(env_path)
print(load)
ENVS = {
    "database": os.getenv("POSTGRES_DB"),
    "host": os.getenv("POSTGRES_HOST")
    "user": os.getenv("POSTGRES_USER"),
    "pass": os.getenv("POSTGRES_PASSWORD"),
    "port": os.getenv("POSTGRES_PORT")
}
print(ENVS)
# def _database_url() -> str:
#     database_url = os.getenv("POSTGRES_DB")
#     if database_url:
#         return database_url

#     return str(
#         URL.create(
#             drivername=os.getenv("POSTGRES_DRIVER", "postgresql+psycopg"),
#             username=os.getenv("POSTGRES_USER"),
#             password=os.getenv("POSTGRES_PASSWORD"),
#             host=os.getenv("POSTGRES_HOST", "localhost"),
#             port=int(os.getenv("POSTGRES_PORT", "5433")),
#             database=os.getenv("POSTGRES_DB", "postgres"),
#         )
#     )

# engine = create_engine(
#     _database_url(),
#     echo=os.getenv("DB_ECHO", "false").lower() == "true",
#     pool_pre_ping=True,
# )


def check_connection() -> bool:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return True


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
