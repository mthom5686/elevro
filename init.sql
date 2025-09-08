-- Users
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crews
CREATE TABLE IF NOT EXISTS crews (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_by INT REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User-Crew mapping
CREATE TABLE IF NOT EXISTS user_crews (
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    crew_id INT REFERENCES crews(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, crew_id)
);

-- Goals
CREATE TABLE IF NOT EXISTS goals (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    metric VARCHAR(50) NOT NULL,
    target_value INT NOT NULL,
    timeframe VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_user_metric UNIQUE (user_id, metric)  -- 🔑 new
);

-- Motivation Messages
CREATE TABLE IF NOT EXISTS motivation_messages (
    id SERIAL PRIMARY KEY,
    crew_id INT REFERENCES crews(id) ON DELETE CASCADE,
    user_id INT REFERENCES users(id) ON DELETE SET NULL,
    message TEXT NOT NULL,
    start_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--Deactivate Users
ALTER TABLE users 
ADD COLUMN IF NOT EXISTS active BOOLEAN DEFAULT TRUE;

-- Demo user + crew
INSERT INTO users (name, email, password_hash)
VALUES ('Demo User', 'demo@elevro.com', '$2b$12$KixwBIkTgF1yd9J7T6YF1O7yFjPXL6TrtoipFO9Yf6aTj8k8kSKpi')
ON CONFLICT (email) DO NOTHING;

INSERT INTO crews (name, created_by)
VALUES ('Demo Crew', 1)
ON CONFLICT DO NOTHING;

INSERT INTO user_crews (user_id, crew_id)
VALUES (1, 1)
ON CONFLICT DO NOTHING;

INSERT INTO goals (user_id, metric, target_value, timeframe)
VALUES
(1, 'protein', 140, 'daily'),
(1, 'workout_volume', 9000, 'weekly'),
(1, 'cardio_minutes', 120, 'weekly')
ON CONFLICT (user_id, metric) DO UPDATE
SET target_value = EXCLUDED.target_value;

INSERT INTO motivation_messages (crew_id, user_id, message, start_date)
VALUES (1, 1, 'Push for 1% better every day!', CURRENT_DATE)
ON CONFLICT DO NOTHING;
