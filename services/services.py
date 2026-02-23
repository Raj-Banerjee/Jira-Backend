# app/services/services.py

from core.database import get_connection
from utils.security import hash_password
from psycopg2 import errors


def register_user(user_data):

    print(type(user_data.password))
    print(user_data.password)
    conn = get_connection()
    cursor = conn.cursor()

    try:
        hashed_pwd = hash_password(user_data.password)

        query = """
            INSERT INTO jira_auth.users (name, email, password_hash)
            VALUES (%s, %s, %s)
            RETURNING id, name, email, is_active, created_at;
        """

        cursor.execute(
            query,
            (user_data.name, user_data.email, user_data.password)
        )

        new_user = cursor.fetchone()
        conn.commit()

        return new_user

    except errors.UniqueViolation:
        conn.rollback()
        raise Exception("Email already exists")

    finally:
        cursor.close()
        conn.close()