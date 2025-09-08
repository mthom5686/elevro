import os
import psycopg2

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "elevro"),
        password=os.getenv("DB_PASS", "secret"),
        dbname=os.getenv("DB_NAME", "elevrodb"),
    )

def get_leaderboard():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT u.name,
               MAX(CASE WHEN g.metric = 'workout_volume' THEN g.target_value END) as workout_volume,
               MAX(CASE WHEN g.metric = 'protein' THEN g.target_value END) as protein,
               MAX(CASE WHEN g.metric = 'cardio_minutes' THEN g.target_value END) as cardio
        FROM users u
        LEFT JOIN goals g ON u.id = g.user_id
        GROUP BY u.name;
    """)
    rows = cur.fetchall()
    conn.close()
    return rows
