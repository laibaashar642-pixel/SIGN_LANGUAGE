#Detection
# │
# ├── __init__()
# ├── predict(frame)
# └── get_boxes(results)
import cv2
from ultralytics import YOLO

class Detection:
    def __init__(self, model_path, conf,source):
        self.source=source
        self.model_path = model_path
        self.model = YOLO(model_path)
        self.conf = conf
    def open_webcam(self,source):
        self.cap = cv2.VideoCapture(source) #opening webcam
        if source == "0":
                 source = 0
        if not self.cap.isOpened():
                    raise RuntimeError("Error: Cannot access the webcam")
                    return
    
    def read(self):
        return self.cap.read()
    def detect(self, frame):
         
          results = self.model.predict(
                source=frame,
                conf=self.conf,
                iou=0.45,
                agnostic_nms=True,
                verbose=False
              


            )
          return results
    def get_boxes(self,results):
        boxes=results[0].boxes
        
        return boxes



    def release(self):
        self.cap.release()
    def show_classes(self,):
        print("Classes:",self.model.names)
    