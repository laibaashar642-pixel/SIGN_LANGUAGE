# Drawer
# │
# └── draw(
#       annotated_frame,
#       x1,
#       y1,
#       x2,
#       y2,
#       label,
#       confidence)
import cv2


class Drawer:
  def draw(self,annotated_frame,x1,y1,x2,y2,label,confidence):
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
        return annotated_frame