# FlowLabs Hormone and Sensitivity Tracker (Garmin + AI)

This project is an experiment in tracking nervous system and hormone-related symptoms using:

- A Garmin watch (Connect IQ app for quick check-ins)
- Garmin Health data (HRV, sleep, temperature, stress)
- A backend API (FastAPI + SQLite)
- AI-assisted reflection and pattern analysis

The goal is to combine three layers of information:

### 1. Subjective data
- Dizziness  
- Vertigo  
- Headache  
- Hot flashes  
- Sugar sensitivity  
- Fatigue  
- Emotional sensitivity  

### 2. Context data
- Estradiol dosing days  
- Antiviral medication (e.g., acyclovir)  
- High-sugar foods  
- Gluten cross-contact  
- Long client / farm work blocks  

### 3. Objective data (from Garmin)
- HRV  
- Sleep stages and quality  
- Stress score  
- Skin temperature (nightly deviation)  
- Heart rate  

---

## System Overview

1. **Garmin Watch App (Connect IQ)**  
   - Vibrates on a schedule  
   - Prompts a 5–10 second symptom check-in  
   - Saves entries locally to sync through Garmin Connect  

2. **Backend API (FastAPI)**  
   - Receives check-ins in JSON format  
   - Stores data in SQLite  
   - Exposes endpoints for retrieval and analysis  

3. **Schemas**  
   - JSON examples defining check-in structure  
   - Used for testing ingestion and integrations  

---

## Directory Structure

```text
ciq-app/           # Connect IQ app source (Monkey C)
backend/           # FastAPI backend + SQLite DB init
schemas/           # JSON example payloads
