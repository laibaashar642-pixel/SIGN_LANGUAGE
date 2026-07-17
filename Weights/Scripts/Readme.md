# Sign Language Alphabet Detection

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

The trained model is automatically downloaded from Google Drive using the `gdown` library before inference.

