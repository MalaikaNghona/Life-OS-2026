
-- 

##  3. DATABASE SCHEMA (docs/DATABASE_SCHEMA.md)

```sql
-- =============================================
-- LIFE OS 2026 - Database Schema
-- PostgreSQL
-- =============================================

-- 1. USERS
CREATE TABLE users (
    id              SERIAL PRIMARY KEY,
    email           VARCHAR(255) UNIQUE NOT NULL,
    password_hash   VARCHAR(255) NOT NULL,
    full_name       VARCHAR(255) NOT NULL,
    nickname        VARCHAR(100),
    avatar_url      TEXT,
    timezone        VARCHAR(50) DEFAULT 'Africa/Johannesburg',
    language        VARCHAR(10) DEFAULT 'en',
    currency        VARCHAR(10) DEFAULT 'ZAR',
    theme           VARCHAR(10) DEFAULT 'light',  -- 'light' or 'dark'
    compact_view    BOOLEAN DEFAULT FALSE,
    two_factor_enabled BOOLEAN DEFAULT FALSE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. NOTIFICATION PREFERENCES
CREATE TABLE notification_preferences (
    id                  SERIAL PRIMARY KEY,
    user_id             INTEGER REFERENCES users(id) ON DELETE CASCADE,
    daily_reminders     BOOLEAN DEFAULT FALSE,
    goal_updates        BOOLEAN DEFAULT FALSE,
    workout_reminders   BOOLEAN DEFAULT FALSE,
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. WORD OF THE YEAR
CREATE TABLE word_of_year (
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER REFERENCES users(id) ON DELETE CASCADE,
    year        INTEGER NOT NULL,
    word        VARCHAR(100) NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, year)
);

-- 4. VISION BOARD
CREATE TABLE vision_board_images (
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER REFERENCES users(id) ON DELETE CASCADE,
    year        INTEGER NOT NULL,
    image_url   TEXT NOT NULL,
    position    INTEGER DEFAULT 0,  -- ordering
    caption     TEXT,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5. GOALS
CREATE TABLE goals (
    id              SERIAL PRIMARY KEY,
    user_id         INTEGER REFERENCES users(id) ON DELETE CASCADE,
    title           VARCHAR(255) NOT NULL,
    description     TEXT,
    progress        DECIMAL(5,2) DEFAULT 0.00,  -- 0.00 to 100.00
    status          VARCHAR(20) DEFAULT 'active',  -- active, completed, paused
    target_date     DATE,
    category        VARCHAR(50),  -- personal, financial, health, etc.
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. GOAL MILESTONES
CREATE TABLE goal_milestones (
    id          SERIAL PRIMARY KEY,
    goal_id     INTEGER REFERENCES goals(id) ON DELETE CASCADE,
    title       VARCHAR(255) NOT NULL,
    is_complete BOOLEAN DEFAULT FALSE,
    completed_at TIMESTAMP,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 7. CALENDAR EVENTS
CREATE TABLE calendar_events (
    id              SERIAL PRIMARY KEY,
    user_id         INTEGER REFERENCES users(id) ON DELETE CASCADE,
    title           VARCHAR(255) NOT NULL,
    description     TEXT,
    start_datetime  TIMESTAMP NOT NULL,
    end_datetime    TIMESTAMP,
    all_day         BOOLEAN DEFAULT FALSE,
    color           VARCHAR(7),  -- hex color
    recurrence      VARCHAR(50),  -- none, daily, weekly, monthly
    category        VARCHAR(50),
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 8. JOURNAL ENTRIES
CREATE TABLE journal_entries (
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER REFERENCES users(id) ON DELETE CASCADE,
    entry_date  DATE NOT NULL,
    mood        VARCHAR(20) NOT NULL,  -- amazing, good, okay, bad, stressed
    content     TEXT,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, entry_date)
);

-- 9. MOOD LOGS (quick mood without journal)
CREATE TABLE mood_logs (
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER REFERENCES users(id) ON DELETE CASCADE,
    log_date    DATE NOT NULL,
    mood        VARCHAR(20) NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 10. GAME PLAN - QUARTERS
CREATE TABLE quarters (
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER REFERENCES users(id) ON DELETE CASCADE,
    year        INTEGER NOT NULL,
    quarter     INTEGER NOT NULL CHECK (quarter BETWEEN 1 AND 4),
    strategy    TEXT,  -- Strategy & Action Plan
    optimization TEXT, -- Optimization & Improvements
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, year, quarter)
);

-- 11. FOCUS AREAS
CREATE TABLE focus_areas (
    id          SERIAL PRIMARY KEY,
    quarter_id  INTEGER REFERENCES quarters(id) ON DELETE CASCADE,
    title       VARCHAR(255) NOT NULL,
    description TEXT,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 12. QUARTER-GOAL LINKS
CREATE TABLE quarter_goals (
    id          SERIAL PRIMARY KEY,
    quarter_id  INTEGER REFERENCES quarters(id) ON DELETE CASCADE,
    goal_id     INTEGER REFERENCES goals(id) ON DELETE CASCADE,
    UNIQUE(quarter_id, goal_id)
);

-- 13. LEARNING CATEGORIES
CREATE TABLE learning_categories (
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name        VARCHAR(100) NOT NULL,  -- Cybersecurity, Finance, School
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 14. COURSES
CREATE TABLE courses (
    id              SERIAL PRIMARY KEY,
    user_id         INTEGER REFERENCES users(id) ON DELETE CASCADE,
    category_id     INTEGER REFERENCES learning_categories(id) ON DELETE SET NULL,
    title           VARCHAR(255) NOT NULL,
    platform        VARCHAR(100),  -- Udemy, Coursera, etc.
    total_modules   INTEGER DEFAULT 0,
    completed_modules INTEGER DEFAULT 0,
    status          VARCHAR(20) DEFAULT 'active',  -- active, completed, paused
    progress        DECIMAL(5,2) DEFAULT 0.00,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 15. FINANCE - TRANSACTIONS
CREATE TABLE transactions (
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER REFERENCES users(id) ON DELETE CASCADE,
    type        VARCHAR(10) NOT NULL,  -- 'income' or 'expense'
    amount      DECIMAL(12,2) NOT NULL,
    category    VARCHAR(100),
    description TEXT,
    transaction_date DATE NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 16. EXPENSE CATEGORIES
CREATE TABLE expense_categories (
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name        VARCHAR(100) NOT NULL,
    color       VARCHAR(7),  -- hex color for charts
    budget      DECIMAL(12,2),
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 17. SAVINGS GOALS
CREATE TABLE savings_goals (
    id              SERIAL PRIMARY KEY,
    user_id         INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name            VARCHAR(255) NOT NULL,
    target_amount   DECIMAL(12,2) NOT NULL,
    current_amount  DECIMAL(12,2) DEFAULT 0.00,
    deadline        DATE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 18. INVESTMENTS / TRADING
CREATE TABLE investments (
    id              SERIAL PRIMARY KEY,
    user_id         INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name            VARCHAR(255) NOT NULL,
    type            VARCHAR(50),  -- stock, crypto, etf, etc.
    amount_invested DECIMAL(12,2) NOT NULL,
    current_value   DECIMAL(12,2) DEFAULT 0.00,
    purchase_date   DATE,
    notes           TEXT,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 19. WORKOUT PROGRAMS
CREATE TABLE workout_programs (
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name        VARCHAR(255) NOT NULL,
    description TEXT,
    is_active   BOOLEAN DEFAULT TRUE,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 20. WORKOUT EXERCISES
CREATE TABLE workout_exercises (
    id              SERIAL PRIMARY KEY,
    program_id      INTEGER REFERENCES workout_programs(id) ON DELETE CASCADE,
    name            VARCHAR(255) NOT NULL,
    sets            INTEGER,
    reps            INTEGER,
    duration_minutes INTEGER,
    day_of_week     INTEGER,  -- 0=Mon, 6=Sun
    order_index     INTEGER DEFAULT 0,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 21. WORKOUT LOGS
CREATE TABLE workout_logs (
    id              SERIAL PRIMARY KEY,
    user_id         INTEGER REFERENCES users(id) ON DELETE CASCADE,
    program_id      INTEGER REFERENCES workout_programs(id) ON DELETE SET NULL,
    log_date        DATE NOT NULL,
    duration_minutes INTEGER,
    notes           TEXT,
    completed       BOOLEAN DEFAULT FALSE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 22. ACHIEVEMENTS
CREATE TABLE achievements (
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER REFERENCES users(id) ON DELETE CASCADE,
    title       VARCHAR(255) NOT NULL,
    description TEXT,
    badge_icon  VARCHAR(50),
    earned_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 23. TODAY'S FOCUS / PRIORITIES
CREATE TABLE daily_priorities (
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER REFERENCES users(id) ON DELETE CASCADE,
    priority_date DATE NOT NULL,
    title       VARCHAR(255) NOT NULL,
    is_complete BOOLEAN DEFAULT FALSE,
    order_index INTEGER DEFAULT 0,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 24. MOTIVATIONAL QUOTES
CREATE TABLE quotes (
    id      SERIAL PRIMARY KEY,
    text    TEXT NOT NULL,
    author  VARCHAR(255),
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE  -- custom quotes
);