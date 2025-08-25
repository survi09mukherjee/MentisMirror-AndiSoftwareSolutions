
<h1 align="center">🧙‍♂️🔍 Mentis Mirror: The Mind Revealer 🧠💭</h1>

---
This repository contains the development progress of **_Mentis Mirror_**, a magical Harry Potter–inspired application that combines **_emotion detection_**, **_IoT-based sensor simulation_**, and **_database logging_** with an immersive frontend UI.


 ---

<div align="center">
  <img width="500" height="600" alt="1" src="https://github.com/user-attachments/assets/37117f03-0998-497c-bc4f-cbfd8930be23" />
</div>


*Mentis Mirror* is an intelligent emotion-aware smart mirror, inspired by the wizarding world of Harry Potter. It detects the user's facial emotions in real-time, logs environmental sensor data (temperature, sound, TVOC, CO₂), and reflects back personalized magical feedback. The prototype combines Machine Learning, Streamlit UI, DeepFace emotion recognition, and MySQL database integration.

---
<div align="center">
  <img width="400" height="500" alt="2" src="https://github.com/user-attachments/assets/72441660-9c13-4ebf-9e48-6777218d6605" />
  <img width="400" height="500" alt="3" src="https://github.com/user-attachments/assets/f148ced5-bbbd-411e-b816-f8e37cba5fa1" />
</div>

---
## ✨ Project Highlights

- 🧠 *Emotion Detection* using DeepFace and OpenCV.  
- 📊 *Sensor Data Logging* (temperature, sound, CO₂, TVOC).  
- 🪄 *Harry Potter-Themed UI* with magical creatures and animations.  
- 🗃 *MySQL Integration* for logging and reviewing emotion-sensor data.  
- 🧾 *Interactive Viewer Tab* to explore historical data entries.  

---

## 🧰 Tech Stack

- *Frontend*: Streamlit (Python), Custom CSS, Animated Effects  
- *Backend*: Python, DeepFace, OpenCV, MySQL  
- *Database*: MySQL (with fallback to local file logging)  
- *Sensors (Simulated)*: ESP32 via Wokwi (for future IoT integration)  

---

## ⚙ Setup Instructions

1. *Clone the repository*:
   ```bash
   git clone https://github.com/survi09mukherjee/MentisMirror-AndiSoftwareSolutions.git
   cd MentisMirror-AndiSoftwareSolutions

2. **Create and activate virtual environment**:

    ```bash
    python -m venv deepface_env
    source deepface_env/bin/activate  # On Windows: deepface_env\Scripts\activate

3. *Install dependencies*:

    ```bash
    pip install streamlit
    pip install deepface
    pip install opencv-python
    pip install mysql-connector-python
    pip install pandas
    pip install pillow
    pip install matplotlib
    pip install numpy
    pip install plotly
    pip install streamlit-option-menu
    pip install datetime
    pip install pygame
    pip install -r requirements.txt

5. **Run the application:

    ```bash
    streamlit run app.py

##  Key Functionalities

- Real-time Emotion Recognition via webcam.

- Magical Mirror UI: Emotions trigger animations, quotes, and popups.

- Environmental Awareness: Sensor values are displayed and logged.

- Log Viewer: Explore historical logs with timestamped data.

- Fallback Logging: If MySQL is not available, data is stored locally.


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
### Day 5 (23nd Aug 2025) — IoT Simulation + Stream Logging 
✅ Added **`shap_explainer.py`** → Script to generate SHAP explanations for model predictions.  
✅ Added **`streamshap.py`** → Streamlit app for interactive SHAP visualization and feature importance.  
✅ Updated documentation to include Day 5 updates.  
🚀 Focus today was on **explainable AI integration** with SHAP for interpretability.

---
### Day 6 (24th Aug 2025) — Voice Tone Analysis Integration  
✅ Added **`train_voice_tone_model.py`** → Script to train ML model for detecting and classifying voice tones.  
✅ Added **`voice_tone_app.py`** → Streamlit app for real-time voice tone analysis and user interaction.  
✅ Added **`voice_tone_model.pkl`** → Pre-trained model file for quick inference without retraining.  
✅ Updated documentation to reflect Day 6 work.  
🚀 Focus today was on **speech emotion recognition via voice tone analysis** for extending multimodal emotion detection.  

---
### Day 7 (25th Aug 2025) — Overall project checking  
✅ Added Magical animations for immersive UX. 
✅ Added Final Harry Potter polish (quotes, animations, transitions).  
🚀 Focus today was on **Checking Overall Code of the Project...** .  

---
## 📂 Branching Info  
- **`frontend-ui` branch** → contains Day 1 frontend work.  
- **`emotion` branch** → contains Day 2 emotion detection work.  
- **`db` branch** → contains Day 3 database + viewer work.  
- **`iot-simulation` branch** → contains Day 4 IoT simulation + streaming integration work.
- **`explainability` branch** → contains Day 5 SHAP explainer (`shap_explainer.py`) and Streamlit SHAP visualization (`streamshap.py`) work.
- **`voice-tone` branch** → contains Day 6 voice tone analysis work with training script (`train_voice_tone_model.py`), Streamlit app (`voice_tone_app.py`), and trained model file (`voice_tone_model.pkl`).
- Merge branches step by step into **`main`** after review.

---

## You can enjoy the animation of the UI/UX of this project created 
## 👩‍💻 Contributors

- *Survi Mukherjee* – Developer, UI Designer, Emotion Logic, Integration
- *Joy Mukherjee* – Developer, UI Designer, Emotion Logic, Integration


## "The Mentis Mirror reveals not the face you wear, but the emotions you dare not share — the truest reflection of your heart and soul, whispered through magic untold."

---

✨ _“Happiness can be found even in the darkest of times, if one only remembers to turn on the light.”_ — Albus Dumbledore  

