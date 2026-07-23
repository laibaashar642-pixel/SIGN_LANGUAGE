#Conceptually this class works like this 
# Camera
# │
# ├── Open Camera
# ├── Read Frame
# └── Release Camera
import cv2
class Camera:
    def __init__(self, source):
      
        if source == "0":
                 source = 0
        self.cap = cv2.VideoCapture(source) #opening webcam
        if not self.cap.isOpened():
                    raise RuntimeError("Error: Cannot access the webcam")
                    return

    def read(self):
        return self.cap.read()

    def release(self):
        self.cap.release()