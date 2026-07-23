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
class Write:

  def writing(self,out,frame_count,annotated_frame):
             self.frame_count=frame_count
             self.out=out
             self.out.write(annotated_frame)
            cv2.imshow('Webcam Feed', self.annotated_frame)
        self.frame_count += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
             return

     def release(self):
        self.out.release()
print("Total frames written:", frame_count)
cv2.destroyAllWindows()
result=writing()