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
        GROUP BY u.name
        ORDER BY u.name;
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def get_goals(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT metric, target_value FROM goals WHERE user_id = %s", (user_id,))
    rows = cur.fetchall()
    conn.close()
    return {metric: value for metric, value in rows}

def save_goals(user_id, goals_dict):
    conn = get_connection()
    cur = conn.cursor()

    for metric, value in goals_dict.items():
        cur.execute("""
            INSERT INTO goals (user_id, metric, target_value, timeframe)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (user_id, metric) 
            DO UPDATE SET target_value = EXCLUDED.target_value;
        """, (user_id, metric, value,
              "daily" if metric == "protein" else "weekly"))

    conn.commit()
    conn.close()
