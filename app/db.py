import os
import psycopg2

def init_db():
    """Init DB connection (placeholder)."""
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "elevro"),
            password=os.getenv("DB_PASS", "secret"),
            dbname=os.getenv("DB_NAME", "elevrodb"),
        )
        conn.close()
        print("✅ Database connected")
    except Exception as e:
        print("❌ Database connection failed:", e)
