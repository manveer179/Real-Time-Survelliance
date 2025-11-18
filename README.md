# Real-Time-Survelliance
📌 Overview

This project implements a Real-Time Surveillance System using the YOLO (You Only Look Once) deep learning model.
The system captures live video from a webcam and performs instant object detection and tracking, making it ideal for security, monitoring, automation, and analytics applications.

🎯 Objectives

Detect and track objects (humans, vehicles, etc.) in real time

Automate surveillance and reduce manual monitoring

Provide fast, accurate, and scalable real-time video analysis

Demonstrate the use of YOLO + Tracking in Python

✨ Features

Real-Time Object Detection

Accurate Multi-Object Tracking (ByteTrack / BOTSort)

Webcam Live Stream Support

720p High-Resolution Processing

Fast Inference using YOLOv8 / Custom Models

Lightweight and Easy to Run

📁 Project Structure
project/
│── tracking.py            # Main script for real-time surveillance
│── yolo12s.pt             # YOLO model file (custom or YOLOv8)
│── README.md              # Project documentation
│── bytetrack.yaml         # Tracker configuration file

🧠 Technologies Used

Python

Ultralytics YOLO (v8 / YOLO-World)
OpenCV
ByteTrack / BOTSort
NumPy

⚙️ Installation
1️⃣ Install Python dependencies
pip install ultralytics opencv-python


If you are using YOLO-World:

pip install supervision

▶️ Usage
Run the Real-Time Surveillance Script

Create a file named tracking.py and add:

from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolo12s.pt")  # Ensure file exists

# Run tracking on webcam with 720p resolution
results = model.track(
    source=0,                # Webcam input
    show=True,               # Display output window
    imgsz=720,               # Input image size (720p)
    tracker="bytetrack.yaml" # Required for tracking
)

🔍 How It Works

The webcam continuously sends video frames.

Each frame is processed by the YOLO model for detection.

ByteTrack tracker assigns unique IDs to objects for continuous tracking.

Bounding boxes, labels, and IDs are displayed in real time on screen.

The feed updates continuously until the program is stopped.

🛡️ Applications

✔ Security surveillance
✔ Smart home or office monitoring
✔ Crowd and activity analysis
✔ Traffic monitoring system
✔ Retail customer tracking
✔ Industrial safety monitoring

🏆 Advantages

Fully automated surveillance

High accuracy using deep learning

Works on both CPU and GPU

Easy to deploy using a simple Python script

Can be extended for multiple camera feeds
