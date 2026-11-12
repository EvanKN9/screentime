import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL, pool_pre_ping=True)


def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print(f"Database connection successful: {result.scalar()}")


if __name__ == "__main__":
    test_connection()