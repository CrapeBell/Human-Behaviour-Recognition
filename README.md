# Human Behavior & Emotion Recognition System

A rule‑based computer vision application built with **Python, OpenCV, and Streamlit** to detect human actions (walking, sitting, waving) and emotions (happy, angry, surprised) in real time **without datasets or pre‑trained models**. The system uses logical heuristics and simulated inputs, making it lightweight, fast, and ideal for **low‑resource environments, prototypes, and educational demonstrations**.

---

## ✨ Features
- Real‑time camera feed with pose & facial landmarks  
- Rule‑based detection (no dataset required)  
- Interactive Streamlit dashboard with animated UI  
- Analytics: session stats, FPS, behavior & emotion distribution, recent activity log  
- Exportable session data for further analysis  

---

## 🛠️ Tech Stack
- Python  
- OpenCV  
- Streamlit  
- Plotly & Pandas  

---

## ⚙️ How It Works
1. **Camera Handler** captures frames from the webcam.  
2. **Behavior Detector** applies heuristic rules to identify actions (e.g., walking, sitting).  
3. **Emotion Detector** analyzes facial features to infer emotions (e.g., happy, surprised).  
4. **Landmark Overlay** draws pose and facial landmarks on the live feed for visualization.  
5. **Analytics Tracker** records detections, calculates session stats, and generates charts.  
6. The **Streamlit Dashboard** displays the live feed, current detections, confidence scores, and interactive analytics in real time.  

---

## 👩‍💻 Team Members
- **Aakriti Mogha** — Project Lead, Computer Vision & Heuristic Design  
- **Anamika Uniyal** — UI/UX & Streamlit Dashboard Development  
- **Aarushi Agrawal** — Analytics & Visualization (Plotly, Pandas)  
- **Anushka Negi** — Testing, Documentation & Integration  

---

## ▶️ Quick Start
```bash
git clone https://github.com/CrapeBell/human-behavior-recognition.git
cd human-behavior-recognition
pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Dashboard Highlights
- **Behavior Distribution**: Pie chart of detected actions  
- **Emotion Distribution**: Bar chart of detected emotions  
- **Recent Activity**: Log of last 10 detections  
- **Session Stats**: Duration, FPS, unique behaviors & emotions  

---


