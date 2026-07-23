# VideoSaver
# │
# ├── __init__()
# ├── create_writer()
# ├── write_frame(frame)
# └── release()

import os 
import cv2
class Video_Saver:
       def __init__(self,save_name,save_dir,cap) :
        self.frame_count=0
        self.cap=cap
        self.save_dir=save_dir
        self.save_name=save_name
        self.out=None
       def create_writer(self):
           
           os.makedirs(self.save_dir, exist_ok=True)
           video_path = os.path.join(self.save_dir, f"{self.save_name}.mp4")
        #Delete process video if its exist
           if os.path.exists(video_path):
            os.remove(video_path)
        # Video properties
           frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
           frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
           fps = 20
           fourcc = cv2.VideoWriter_fourcc(*"mp4v")

           self.out = cv2.VideoWriter(
            video_path,
            fourcc,
            fps,
            (frame_width, frame_height)
        )
           print(f"Saving video to: {video_path}")
           print("Frame size:", frame_width, frame_height)
           print("VideoWriter opened:", self.out.isOpened())
           self.frame_count = 0  

        


       def write_frame(self,annotated_frame):
           
            self.out.write(annotated_frame)
          
            self.frame_count += 1


       def release(self):
            print("Total frames written:", self.frame_count)
            if self.out:
             self.out.release()
            else:
                print("Not Releasing")