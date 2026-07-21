<!-- # Sign Language Alphabet Detection

## Overview

This project performs real-time American Sign Language (ASL) alphabet detection using a custom-trained YOLO model. The system recognizes hand gestures (A–Z) from a webcam and displays the detected alphabet with a bounding box and confidence score.

## Features

- Real-time ASL alphabet detection
- YOLO-based object detection
- Bounding box and confidence score visualization
- Automatic model download using `gdown`
- Webcam support

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --task detect --model Weights/best_sign.pt --source 0 --project runs --save-dir Results
```

## Note

The trained model is automatically downloaded from Google Drive using the `gdown` library before inference. -->
# 
 ASL Alphabet Detection — Real-Time Sign Language Recognition

A real-time computer vision system that detects American Sign Language (ASL) alphabet gestures (A–Z) from a live webcam feed using a custom-trained YOLO object detection model.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![YOLO](https://img.shields.io/badge/Model-YOLO-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📌 Overview

This project uses a custom-trained YOLO model to detect and classify ASL hand gestures in real time. It draws bounding boxes around detected hands and labels them with the predicted letter and confidence score, enabling instant sign-to-text recognition through a standard webcam — no specialized hardware required.

## 💡 Why This Matters (Real-World Use Case)

Sign language recognition technology has practical applications in:
- **Accessibility tools** — bridging communication between deaf/hard-of-hearing individuals and non-signers
- **Educational platforms** — real-time feedback for people learning ASL
- **Assistive kiosks** — contactless interaction at public service points (airports, hospitals, government offices)

## ✨ Features

- 🎥 Real-time detection via webcam
- 🎯 Custom-trained YOLO model on the American Sign Language Letters dataset
- 📦 Bounding box + label + confidence score visualization
- ⚙️ Modular, class-based, CLI-driven architecture (`argparse`)
- ☁️ Automatic model download via `gdown` (no manual weight management)

## 📊 Model Performance

| Metric | Score |
|---|---|
| Precision | 93.8% |
| Recall | 82.8% |
| mAP50 | 82.0% |
| mAP50-95 | 68.9% |

## 🛠️ Tech Stack

- **Language:** Python
- **Detection Model:** YOLO (Ultralytics)
- **Computer Vision:** OpenCV
- **Dataset:** [American Sign Language Letters](https://universe.roboflow.com/david-lee-d0rhs/american-sign-language-letters) (Roboflow)
- **CLI:** argparse

## 📂 Project Structure