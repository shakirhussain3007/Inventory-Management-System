from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import text

from app.config.settings import settings

DATABASE_URL = (
    f"mysql+pymysql://"
    f"{settings.DB_USER}:"
    f"{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:"
    f"{settings.DB_PORT}/"
    f"{settings.DB_NAME}"
                            # mysql+pymysql://root:1234@localhost:3306/inventory_db
)

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def test_database_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            print("Database Connected Successfully")
    except Exception as e:
        print("Db Connection Failed")
        print(e)