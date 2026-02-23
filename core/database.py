import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def get_connection():
    return psycopg2.connect(
        DATABASE_URL,
        cursor_factory=RealDictCursor
    )


# import psycopg2
# from psycopg2 import pool
# from .config import DATABASE_URL

# connection_pool = pool.SimpleConnectionPool(
#     1,
#     10,
#     dsn=DATABASE_URL
# )

# def get_db_connection():
#     conn = connection_pool.getconn()
#     try:
#         yield conn
#     finally:
#         connection_pool.putconn(conn)

# app/core/database.py
