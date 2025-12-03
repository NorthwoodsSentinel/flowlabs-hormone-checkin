# FlowLabs Hormone and Sensitivity Tracker (Garmin + AI)

This project is an experiment in tracking nervous system and hormone-related symptoms using:

- A Garmin watch (Connect IQ app for quick check-ins)
- Garmin Health data (HRV, sleep, temperature, stress)
- A backend API (FastAPI + SQLite)
- AI-assisted reflection and pattern analysis

The goal is to combine three layers of information:

1. Subjective data
   - Dizziness
   - Vertigo
   - Headache
   - Hot flashes
   - Sugar sensitivity
   - Fatigue
   - Emotional sensitivity

2. Context data
   - Estradiol dosing days
   - Antiviral medication
   - High-sugar foods
   - Possible gluten cross-contact
   - Long client / farm work blocks

3. Objective data (from Garmin)
   - HRV
   - Sleep stages and quality
   - Stress score
   - Skin temperature (nightly deviation)
   - Heart rate

---

## System Overview

1. Garmin Watch App (Connect IQ)
   - Vibrates on a schedule
   - Prompts a 5–10 second symptom check-in
   - Saves entries locally to sync through Garmin Connect

2. Backend API (FastAPI)
   - Receives check-ins in JSON format
   - Stores data in SQLite
   - Exposes endpoints for retrieval and analysis

3. Schemas
   - JSON examples defining check-in structure
   - Used for testing ingestion and integrations

---

## Directory Structure

ciq-app/           - Connect IQ app source (Monkey C)
backend/           - FastAPI backend + SQLite DB init
schemas/           - JSON example payloads
sync/              - Placeholder script for ingestion from exports

---

## Getting Started (Backend)

Install dependencies:

    cd backend
    pip install -r requirements.txt

Initialize the SQLite database:

    python db_init.py

Start the API:

    uvicorn main:app --reload

Test ingestion with the example JSON:

    curl -X POST \
      http://localhost:8000/ingest/hormone-checkin \
      -H "Content-Type: application/json" \
      -d @../schemas/checkin_example.json

View latest entries:

    curl http://localhost:8000/checkins/latest

---

## Architecture Overview

    [Garmin Watch]
         |
         |  (Connect IQ Hormone Check In App)
         v
    [Garmin Connect / Garmin Health Data]
         |
         |  (exports or API)
         v
    [Sync Script]
    sync/garmin_to_flowlabs.py
         |
         |  HTTP POST /ingest/hormone-checkin
         v
    [FastAPI Backend]
    backend/main.py
         |
         |  INSERT
         v
    [SQLite DB]
    flowlabs_hormone.db
         |
         +--> Queries, analysis, AI-assisted reflection

---

## Purpose and Disclaimer

This is not medical software and is not intended to diagnose, treat, cure, or prevent any disease.

It is a personal research and pattern-finding tool designed to explore how:

- Somatic cues
- Hormonal patterns
- Vertigo and dizziness
- Sleep
- Sugar sensitivity
- Emotional states

line up with wearable data from Garmin devices.

Always consult qualified professionals for medical and mental health concerns.
