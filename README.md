# GhostTrack — The Journey Log

> **Live Link:** [https://ghosttrack-journey-git-main-leharinshainsha05-stacks-projects.vercel.app/](https://ghosttrack-journey-git-main-leharinshainsha05-stacks-projects.vercel.app/)

A comprehensive blind-spot safety system for Indian heavy commercial vehicles, compliant with the approaching AIS-186 BSIS mandate. This log details the journey from a simple concept document to a fully functional, integrated system.

---

## 🚀 Key Highlights & System Architecture

- **Dual-Model Vision Pipeline:** Powered by a Raspberry Pi 5 running a custom-trained YOLOv8n model for India-specific vehicle classes (auto-rickshaw, tractor, e-rickshaw, LCVs) and COCO-pretrained weights for pedestrians and cyclists.
- **24GHz mmWave Radar:** Implemented Waveshare S3KM1110 mmWave sensors with a custom state-machine binary parser in C++ on an ESP32-S3.
- **Directional Haptic Steering Wheel:** Custom-designed and 3D-printed steering wheel embedded with dual 10mm ERM coin vibration motors (LEDC PWM controlled) for tactile warning alerts.
- **Hardware-in-the-Loop Scale Model:** A 1:10 scale model of an Indian heavy commercial vehicle housing the entire hardware setup, dual CSI cameras, and integrated wiring.
- **Pi ↔ ESP32 UART Link:** High-frequency serial cross-communication protocol bridging the Pi 5's Python inference engine and the ESP32-S3's haptic fusion logic.

---

## 📂 Supporting Materials

- **GitHub Organisation:** [GhostTrack-Team](https://github.com/GhostTrack-Team)
- **Kaggle Notebook:** [YOLOv8 training pipeline](https://www.kaggle.com/code/leharinnisha/ghosttrack)
- **Project Site:** [ghosttruck.onrender.com](https://ghosttruck.onrender.com)
- **3D Model Viewer:** [Three.js scale-truck viewer](https://ghosttrack-team.github.io/indian-lorry-blindspot/)

---

## 🛠️ Build Status
All core subsystems are fully functional and integrated end-to-end:
- **Pi 5 dual-camera pipeline:** Functional (Picamera2 + YOLOv8n + custom ONNX + Flask MJPEG)
- **ESP32-S3 firmware:** Functional (Dual radar, haptics, SoftAP dashboard)
- **UART physical link:** Connected and functional
- **Live radar system testing:** Verified live in combined system
