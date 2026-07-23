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
        print("Model loaded from:", model_path)
        print("Classes:", self.model.names)
    def open_webcam(self,source):
        if source == "0":
                 source = 0
        self.cap = cv2.VideoCapture(source) #opening webcam
        if not self.cap.isOpened():
                    raise RuntimeError("Error: Cannot access the webcam")
                    return
    
    def read(self):
        return self.cap.read()
    def detect(self, source):
         
          results = self.model.predict(
                source=source,
                conf=self.conf,
                iou=0.45,
                agnostic_nms=True,
                verbose=False
              


            )
          return results
    def get_boxes(self,results):
        boxes_list = []
        boxes=results[0].boxes
        
        boxes = results[0].boxes

        for box in boxes:
          x1, y1, x2, y2 = map(int, box.xyxy[0])
          conf = float(box.conf[0])
          cls_id = int(box.cls[0])
          label = self.model.names[cls_id]

          boxes_list.append({
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,
            "label": label,
            "conf": conf
        })

        return boxes_list
        
        return boxes



    def release(self):
        self.cap.release()
    def show_classes(self,):
        print("Classes:",self.model.names)
    