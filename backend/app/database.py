"""
Database Connection & Session Factory
Supports PostgreSQL (default production) and SQLite (zero-friction local development).
"""

# © 2026 BLUEGUN
# Original project code and implementation.
# Third-party libraries and materials remain subject to their respective licenses.
# See /credits (Copyright & Sources page) for full attribution.


import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Load environment variables from .env
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DB_PATH = os.path.join(BASE_DIR, "transfer_market.db").replace("\\", "/")
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DEFAULT_DB_PATH}")

# If SQLite is configured with relative path, normalize it
if DATABASE_URL.startswith("sqlite:///./"):
    rel = DATABASE_URL.replace("sqlite:///./", "")
    abs_path = os.path.join(BASE_DIR, rel).replace("\\", "/")
    DATABASE_URL = f"sqlite:///{abs_path}"

# SQLite requires check_same_thread=False, PostgreSQL does not
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    FastAPI Dependency that yields a SQLAlchemy database session and ensures proper closure.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
