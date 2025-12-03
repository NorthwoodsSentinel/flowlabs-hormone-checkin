from datetime import datetime
import sqlite3
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


DB_PATH = "flowlabs_hormone.db"
app = FastAPI(title="FlowLabs Hormone and Sensitivity API")


class HormoneCheckIn(BaseModel):
    user_id: str
    device_id: Optional[str] = None
    timestamp_utc: datetime

    checkin_type: Optional[str] = None
    cycle_day: Optional[int] = None
    is_estradiol_day: Optional[bool] = None
    took_antiviral: Optional[bool] = None

    dizziness: Optional[int] = None
    vertigo: Optional[int] = None
    headache: Optional[int] = None
    nausea: Optional[int] = None
    sugar_sensitivity: Optional[int] = None
    sensory_overload: Optional[int] = None
    fatigue: Optional[int] = None
    emotional_sensitivity: Optional[int] = None

    hot_flash_intensity: Optional[int] = None
    hot_flash_duration: Optional[str] = None
    nightly_skin_temp: Optional[float] = None

    high_sugar_food: Optional[bool] = None
    possible_gluten_crosscontact: Optional[bool] = None
    strong_odors: Optional[bool] = None
    long_client_block: Optional[bool] = None

    notes: Optional[str] = None


def get_db():
    return sqlite3.connect(DB_PATH)


@app.post("/ingest/hormone-checkin")
def ingest_checkin(checkin: HormoneCheckIn):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO hormone_checkins (
            user_id, device_id, timestamp_utc,
            checkin_type, cycle_day, is_estradiol_day, took_antiviral,
            dizziness, vertigo, headache, nausea, sugar_sensitivity,
            sensory_overload, fatigue, emotional_sensitivity,
            hot_flash_intensity, hot_flash_duration, nightly_skin_temp,
            high_sugar_food, possible_gluten_crosscontact, strong_odors,
            long_client_block, notes
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            checkin.user_id,
            checkin.device_id,
            checkin.timestamp_utc.isoformat(),
            checkin.checkin_type,
            checkin.cycle_day,
            int(checkin.is_estradiol_day or 0),
            int(checkin.took_antiviral or 0),
            checkin.dizziness,
            checkin.vertigo,
            checkin.headache,
            checkin.nausea,
            checkin.sugar_sensitivity,
            checkin.sensory_overload,
            checkin.fatigue,
            checkin.emotional_sensitivity,
            checkin.hot_flash_intensity,
            checkin.hot_flash_duration,
            checkin.nightly_skin_temp,
            int(checkin.high_sugar_food or 0),
            int(checkin.possible_gluten_crosscontact or 0),
            int(checkin.strong_odors or 0),
            int(checkin.long_client_block or 0),
            checkin.notes,
        ),
    )
    conn.commit()
    conn.close()
    return {"status": "ok"}


@app.get("/checkins/latest")
def latest_checkins(limit: int = 20):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT
            id, user_id, device_id, timestamp_utc,
            dizziness, vertigo, headache, nausea,
            sugar_sensitivity, sensory_overload, fatigue,
            emotional_sensitivity, hot_flash_intensity, nightly_skin_temp
        FROM hormone_checkins
        ORDER BY timestamp_utc DESC
        LIMIT ?
        """,
        (limit,),
    )
    rows = cur.fetchall()
    conn.close()

    result = []
    for row in rows:
        result.append(
            {
                "id": row[0],
                "user_id": row[1],
                "device_id": row[2],
                "timestamp_utc": row[3],
                "dizziness": row[4],
                "vertigo": row[5],
                "headache": row[6],
                "nausea": row[7],
                "sugar_sensitivity": row[8],
                "sensory_overload": row[9],
                "fatigue": row[10],
                "emotional_sensitivity": row[11],
                "hot_flash_intensity": row[12],
                "nightly_skin_temp": row[13]
            }
        )

    return result
