# Sign Language Detection using YOLO

## Overview

This project is a real-time Sign Language Detection system developed using the Ultralytics YOLO framework and OpenCV. It detects sign language gestures from a webcam, video, or image and displays the detected classes with bounding boxes and confidence scores. The project is designed with a modular architecture to improve readability, reusability, and maintainability.

---

## Demo

### Preview (GIF)

<img width="480" height="360" alt="Sign Language Detection Demo" src="https://github.com/user-attachments/assets/bb3c3b71-cac1-4556-875b-f3d97b7b8111" />

### Full Video

https://github.com/user-attachments/assets/6f218635-88bc-43ca-8668-b16a039dea2c

---

## Features

- Real-time webcam detection
- Video and image inference
- YOLO-based object detection
- Bounding box visualization
- Confidence score display
- Save processed video automatically
- Modular and reusable architecture
- Command-line argument support

---

## Project Structure

```
Sign_Language/
│
├── main.py
├── requirements.txt
├── README.md
│
├── Utils/
│   └── args.py
│
├── Scripts/
│   ├── detect.py
│   ├── drawer.py
│   ├── save_video.py
│   └── test_image.py
│
├── Weights/
│   └── best_words.pt
│
├── outputs/
│
└── Results/
```

---

## Architecture

```
args.py
   │
   ▼
main.py
   │
   ├──────────────┐
   │              │
   ▼              ▼
Detection      Video_Saver
   │
   ├── open_webcam()
   ├── read()
   ├── detect()
   └── get_boxes()
          │
          ▼
       Drawer
          │
          ▼
   Annotated Frame
          │
          ▼
   Video_Saver.write_frame()
          │
          ▼
     Output Video
```

---

## Workflow

```
Input
(Webcam / Image / Video)
          │
          ▼
OpenCV Capture
          │
          ▼
YOLO Detection
          │
          ▼
Extract Bounding Boxes
          │
          ▼
Draw Bounding Boxes
          │
          ▼
Display Frame
          │
          ▼
Save Output Video
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/laibaashar642-pixel/SIGN_LANGUAGE.git
```

Move into the project directory

```bash
cd SIGN_LANGUAGE
```

Create a virtual environment

### Windows

```bash
python -m venv .venv
```

Activate the environment

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Model Weights

Trained model weights are not included in this GitHub repository due to file size restrictions. They are hosted on Google Drive and can be downloaded using the `gdown` library.

Install `gdown`:

```bash
pip install --upgrade --no-cache-dir gdown
```

Download the weights folder (Python):

```python
import gdown

gdown.download_folder(
    "https://drive.google.com/drive/folders/1HKOsC-PLztQSxn0p4_V3BlQFQqnTuqg5",
    output="drive_download",
    quiet=False,
    use_cookies=False
)
```

> Note: `use_cookies=False` avoids a common Colab/gdown authentication issue where folder downloads silently return an HTML error page instead of the actual files.

This will create a `drive_download/` folder containing `Results/`, `Sample_Test/`, and `Weights/` (with `best_sign.pt` and `best_words.pt`).

Copy the trained model into the project's `Weights/` folder so it matches the structure used in the Usage section below:

```bash
cp drive_download/Weights/best_words.pt Weights/
```

After this step, your project structure will match the one shown above, with `Weights/best_words.pt` ready to use.

---

## Usage

### Webcam Detection

```bash
python main.py --task detect --model "Weights/best_words.pt" --source 0 --project "runs/detect" --save-dir "outputs" --conf 0.5
```

### Video Detection

```bash
python main.py --task detect --model "Weights/best_words.pt" --source "video.mp4" --project "runs/detect" --save-dir "outputs" --conf 0.5
```

### Image Detection

```bash
python main.py --task detect --model "Weights/best_words.pt" --source "image.jpg" --project "runs/detect" --save-dir "outputs" --conf 0.5
```

---

## Output

The processed output video is automatically saved in

```
outputs/
```

---

## Technologies Used

- Python
- OpenCV
- Ultralytics YOLO
- NumPy

---

## Future Improvements

- Multi-person sign language detection
- Object tracking integration
- Pose estimation
- GUI support
- REST API deployment
- Model optimization for edge devices

---

## Author

Laiba Ashar
