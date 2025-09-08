-- Users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crews table
CREATE TABLE IF NOT EXISTS crews (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_by INT REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User-Crew membership (many-to-many)
CREATE TABLE IF NOT EXISTS user_crews (
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    crew_id INT REFERENCES crews(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, crew_id)
);

-- Goals per user (persist across all crews)
CREATE TABLE IF NOT EXISTS goals (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    metric VARCHAR(50) NOT NULL,       -- e.g. "protein", "workout_volume"
    target_value INT NOT NULL,
    timeframe VARCHAR(20) NOT NULL,    -- "daily", "weekly"
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Motivation messages (crew-specific, rotating weekly)
CREATE TABLE IF NOT EXISTS motivation_messages (
    id SERIAL PRIMARY KEY,
    crew_id INT REFERENCES crews(id) ON DELETE CASCADE,
    user_id INT REFERENCES users(id) ON DELETE SET NULL,
    message TEXT NOT NULL,
    start_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Demo data
INSERT INTO users (name, email, password_hash) 
VALUES ('Demo User', 'demo@elevro.com', 'hashedpassword')
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
ON CONFLICT DO NOTHING;

INSERT INTO motivation_messages (crew_id, user_id, message, start_date)
VALUES (1, 1, 'Push for 1% better every day!', CURRENT_DATE)
ON CONFLICT DO NOTHING;
