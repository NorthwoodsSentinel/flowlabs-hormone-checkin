import sqlite3

DB_PATH = "flowlabs_hormone.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS hormone_checkins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            device_id TEXT,
            timestamp_utc TEXT NOT NULL,

            checkin_type TEXT,
            cycle_day INTEGER,
            is_estradiol_day INTEGER,
            took_antiviral INTEGER,

            dizziness INTEGER,
            vertigo INTEGER,
            headache INTEGER,
            nausea INTEGER,
            sugar_sensitivity INTEGER,
            sensory_overload INTEGER,
            fatigue INTEGER,
            emotional_sensitivity INTEGER,

            hot_flash_intensity INTEGER,
            hot_flash_duration TEXT,
            nightly_skin_temp REAL,

            high_sugar_food INTEGER,
            possible_gluten_crosscontact INTEGER,
            strong_odors INTEGER,
            long_client_block INTEGER,

            notes TEXT
        );
        """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print(f"Initialized database at {DB_PATH}")
