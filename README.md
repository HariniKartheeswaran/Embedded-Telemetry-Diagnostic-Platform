# Embedded Observability System

## 🚀 Overview
A real-time embedded system that collects sensor data using Arduino and processes it using a Python-based diagnostic engine.

## 🔧 Features
- Multi-sensor data acquisition (temperature, sound, tilt)
- Real-time telemetry via serial communication
- Structured log parsing
- AI-based diagnostic interpretation
- CI/CD pipeline for firmware validation

## 🧠 Architecture
Sensors → Arduino → Serial (UART) → Python → Diagnosis

## ⚙️ Tech Stack
- Arduino (C/C++)
- Python (pyserial)
- Embedded Systems
- GitHub Actions (CI/CD)

## 📊 Example Output
TEMP:600,SOUND:200,TILT:0,STATE:TEMP_HIGH  
→ Overheating → Check environment

## 📌 Key Learning
- Microcontroller + peripherals interfacing
- Real-time data processing
- Debugging via structured telemetry
- DevOps integration for embedded systems