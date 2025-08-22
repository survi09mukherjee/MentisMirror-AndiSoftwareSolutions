# 🌟 Mentis Mirror — Harry Potter Themed Emotion & Sensor Logging App  

This repository contains the development progress of **Mentis Mirror**, a magical Harry Potter–inspired application that combines **emotion detection, IoT-based sensor simulation, and database logging** with an immersive frontend UI.  

---

## 📅 Development Log  

### Day 1 (19th Aug 2025) — Frontend Setup  
✅ Set up **frontend UI structure** in Streamlit.  
✅ Designed **Harry Potter themed magical items & layout**.  
✅ Implemented **modal-style popups and hover effects** for items.  
✅ Added placeholders for dynamic **emotion + sensor integration**.  

---

### Day 2 (20th Aug 2025) — Emotion Detection Integration  
✅ Created new branch **`emotion`** for Day 2 work.  
✅ Integrated **DeepFace emotion detection pipeline**.  
✅ Added **image upload & webcam capture option** for emotion recognition.  
✅ Displayed **real-time detected emotion** in frontend UI.  
✅ Prepared framework for **logging detected emotions + sensor data** to database.  
✅ Synced frontend placeholders with **basic emotion output** (ready for full integration).  

---

### Day 3 (21st Aug 2025) — Database Integration  
✅ Created new branch **`database`** for backend work.  
✅ Implemented **`db_utils.py`** for MySQL connection + fallback to text file storage.  
✅ Designed **database schema (`mirror_logs` table)** for emotion + sensor data logging.  
✅ Integrated **logging button** in frontend to store detected values.  
✅ Added **basic error handling** for DB connection failures.  
✅ Verified first successful emotion + sensor log entry in MySQL.    
✅ Built new **Viewer Tab** in Streamlit to display saved logs.  
✅ Enabled **data fetch from MySQL** (or text file if DB unavailable).  
✅ Added **interactive table** to view logged emotions + sensor values.  
✅ Synced Viewer tab with **real-time updates after logging**.  
✅ Tested end-to-end pipeline → **Emotion detection + sensor simulation → Logging → Viewer tab**.  
✅ Codebase cleanup and structured repo for clarity.  

---

### Day 4 (22nd Aug 2025) — IoT Simulation + Stream Logging  
✅ Created new branch **`iot-simulation`** for IoT work.  
✅ Added **`main.c`** (ESP32 code) and **`wokwi-custom.json`** (simulation config) for **Wokwi-based sensor simulation**.  
✅ Implemented **sensor readout for temperature, humidity, sound, light, gas, and custom sensors**.  
✅ Connected ESP32 simulated outputs to **Streamlit frontend** using new **`streamlog.py`** module.  
✅ Integrated **real-time sensor streaming with emotion logs**.  
✅ Verified successful logging of **sensor + emotion data together** into database and text logs.  
✅ Synced simulation outputs with **frontend magical UI** for immersive interaction.  

---

## 🔮 Features in Progress    
- Magical sound effects + animations for immersive UX.  
- Final Harry Potter polish (quotes, animations, transitions).  

---

## 🚀 Next Steps  
- Enhance **real-time graphing + charts** in frontend from simulation.   
- Add **sound + magical animations** to enhance experience.  

---

## 📂 Branching Info  
- **`frontend-ui` branch** → contains Day 1 frontend work.  
- **`emotion` branch** → contains Day 2 emotion detection work.  
- **`db` branch** → contains Day 3 database + viewer work.  
- **`iot-simulation` branch** → contains Day 4 IoT simulation + streaming integration work.  
- Merge branches step by step into **`main`** after review.  

---

✨ _“Happiness can be found even in the darkest of times, if one only remembers to turn on the light.”_ — Albus Dumbledore  
