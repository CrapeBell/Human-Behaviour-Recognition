# Human Behaviour Recognition

A lightweight computer vision prototype for recognizing human actions and facial emotions from a live camera feed. The project explores rule-based behavior detection, landmark-driven analysis, and an interactive Streamlit dashboard without relying on a large training dataset.

## Overview

The system is designed around two complementary signals:

- **Body/pose analysis** for actions such as sitting, standing, walking, and waving
- **Facial analysis** for simple emotion categories such as happy, angry, and surprised
- **Interactive analytics** for viewing detected behavior, emotion distribution, session activity, and performance information

The project is intended as a practical computer-vision prototype and learning project, with an emphasis on lightweight processing and interpretable detection rules.

## Key Features

- Real-time camera input
- Pose and facial landmark processing
- Rule-based behavior detection
- Emotion classification using visual features
- Streamlit-based dashboard
- Session-level behavior and emotion analytics
- Activity logging and visualization

## How It Works

The architecture below is intentionally centered so the main input and output stages line up with the combined processing branches:

```text
                         Camera Input
                              │
                              ▼
                       Frame Processing
                              │
                 ┌────────────┴────────────┐
                 ▼                         ▼
           Pose Analysis              Face Analysis
                 │                         │
                 ▼                         ▼
          Behavior Rules             Emotion Rules
                 │                         │
                 └────────────┬────────────┘
                              ▼
                     Detection Results
                              │
                              ▼
                   Streamlit Dashboard
                              │
                              ▼
                    Session Analytics
```

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| OpenCV | Camera and image processing |
| Streamlit | Interactive application interface |
| Pandas | Data handling and analytics |
| Plotly | Visualization |

## Project Structure

```text
.
├── app.py
├── cam_handler.py
├── pose_behavior.py
├── emotion_engine.py
├── dashboard_metrics.py
├── test_behavior.py
├── test_emotion.py
├── requirements.txt
└── README.md
```

## My Contribution

**Aarushi Agrawal — Analytics & Visualization**

- Worked on the analytics and visualization layer
- Used Pandas for session-level data handling
- Used Plotly for presenting behavior and emotion distributions
- Contributed to testing, integration, and project documentation

## What This Project Demonstrates

- Real-time computer-vision workflow design
- Image and camera-frame processing
- Landmark-based reasoning
- Rule-based classification
- Data collection and session analytics
- Building an interactive Python application

## Project Status

This repository represents a lightweight prototype/academic project focused on demonstrating the computer-vision workflow and dashboard concept. The detection approach is intentionally rule-based rather than a production-grade trained recognition system.

## Future Improvements

- Replace heuristic rules with trained models
- Add more robust validation and test coverage
- Improve detection under different lighting and camera conditions
- Add model-confidence calibration
- Containerize and deploy the application

## Author

**Aarushi Agrawal**

- GitHub: [CrapeBell](https://github.com/CrapeBell)
- LinkedIn: [Aarushi Agrawal](https://linkedin.com/in/aarushi-agrawal-3b2136279)
