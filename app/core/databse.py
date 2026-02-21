import psycopg2
from psycopg2 import pool
from .config import DATABASE_URL

connection_pool = pool.SimpleConnectionPool(
    1,
    10,
    dsn=DATABASE_URL
)

def get_db_connection():
    conn = connection_pool.getconn()
    try:
        yield conn
    finally:
        connection_pool.putconn(conn)