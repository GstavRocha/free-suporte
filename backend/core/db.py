from collections.abc import Generator
from pathlib import Path
import os

from dotenv import load_dotenv
from sqlalchemy import text
from sqlalchemy.engine import URL
from sqlmodel import Session, create_engine

BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")


def _database_url() -> URL:
    return URL.create(
        drivername="postgresql+psycopg",
        username=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=int(os.getenv("POSTGRES_PORT", "5433")),
        database=os.getenv("POSTGRES_DB"),
    )

engine = create_engine(_database_url(), pool_pre_ping=True)

def check_connection() -> bool:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return True


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
