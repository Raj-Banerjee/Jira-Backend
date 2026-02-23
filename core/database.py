import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
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
