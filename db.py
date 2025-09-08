import os
import psycopg2
import bcrypt

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "elevro"),
        password=os.getenv("DB_PASS", "secret"),
        dbname=os.getenv("DB_NAME", "elevrodb"),
    )

def get_user_by_email(email: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, password_hash FROM users WHERE email = %s AND active = TRUE", (email,))
    row = cur.fetchone()
    conn.close()
    return row  # (id, name, email, hash)

def verify_password(plain_pw: str, hashed_pw: str) -> bool:
    return bcrypt.checkpw(plain_pw.encode("utf-8"), hashed_pw.encode("utf-8"))
