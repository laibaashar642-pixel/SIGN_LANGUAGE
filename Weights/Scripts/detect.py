# import cv2
# from ultralytics import YOLO
# print("Model Loaded Successfully!")

# class Detection:
    
#     def __init__(self,model_path,conf) :
#         self.model_path=model_path
#         self.model=YOLO(model_path)
#         self.conf=conf
  
#     def language_detection(self,save_dir,project,source,save_name="Output"):
 
#         cap = cv2.VideoCapture(source)
  
#         if not cap.isOpened():
#          print("Error: Cannot access the webcam")
#          exit()
#         while True:
#    # Capture frame-by-frame
#           ret, frame = cap.read()
#           if not ret:
#             print("Error: Failed to capture frame")
#             break
#           results=self.model.predict(
#             name=save_name,
#             project=save_dir,
#             source=frame,
#             conf=self.conf
#         )
     
#         cv2.imshow('Webcam Feed', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#          break
#    # Display the captured frame
    

#         cap.release()
#         cv2.destroyAllWindows()
      


import cv2
from ultralytics import YOLO
print("Model Loaded Successfully!")

class Detection:
    def __init__(self, model_path, conf):
        self.model_path = model_path
        self.model = YOLO(model_path)
        self.conf = conf

    def language_detection(self, save_dir, project, source, save_name="Output"):
        print("Classes:",self.model.names)
        if source == "0":
         source = 0
        cap = cv2.VideoCapture(source)
        if not cap.isOpened():
            print("Error: Cannot access the webcam")
            exit()
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture frame")
                break
            results = self.model.predict(
                name=save_name,
                project=save_dir,
                source=frame,
                conf=self.conf,
              

            )
            #To drawing bounded boxes from cv2 
            annotated_frame=frame.copy()
            for box in results[0].boxes:

               x1, y1, x2, y2 = map(int, box.xyxy[0])

               conf = float(box.conf[0])

               cls = int(box.cls[0])

               label = self.model.names[cls]

               cv2.rectangle(
                annotated_frame,
                (x1, y1),
                (x2, y2),
                (0,255,0),
             2
    )

               cv2.putText(
               annotated_frame,
               f"{label} {conf:.2f}",
               (x1, y1-10),
               cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
               (0,255,0),
                2
    )

            print(results[0].boxes)
            cv2.imshow('Webcam Feed', annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
             break
        cap.release()
        cv2.destroyAllWindows()
            
#             results = self.model.predict(
#     source=frame,
#     conf=self.conf,
#     verbose=False
# )

        
