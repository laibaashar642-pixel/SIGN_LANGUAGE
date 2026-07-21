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
      

import os
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
        cap = cv2.VideoCapture(source) #opening webcam
        if not cap.isOpened():
            print("Error: Cannot access the webcam")
            return
            # cap = cv2.VideoCapture(source)

        

        # Create output directory for saving the video
        os.makedirs(save_dir, exist_ok=True)

        # Video properties
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = 20

        # Video writer
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        video_path = os.path.join(save_dir, f"{save_name}.mp4")

        out = cv2.VideoWriter(
            video_path,
            fourcc,
            fps,
            (frame_width, frame_height)
        )

        print(f"Saving video to: {video_path}")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture frame")
                break
            results = self.model.predict(
                
                
                source=frame,
                conf=self.conf,
              

            )
            print("Detections:", len(results[0].boxes))
            #To drawing bounded boxes from cv2 
            annotated_frame=frame.copy()
            for box in results[0].boxes:

               x1, y1, x2, y2 = map(int, box.xyxy[0])

               confidence = float(box.conf[0])

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
               f"{label} {confidence:.2f}",
               (x1, y1-10),
               cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
               (0,255,0),
                2
    )

            # print(results[0].boxes)
            out.write(annotated_frame)
            cv2.imshow('Webcam Feed', annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
             break
        cap.release()
        out.release()
        cv2.destroyAllWindows()
            
#             results = self.model.predict(
#     source=frame,
#     conf=self.conf,
#     verbose=False
# )

        
