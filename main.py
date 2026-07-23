

# # args.py
# #    |
# #    ↓
# # main.py
# #    |
# #    ├── Detection
# #    │       |
# #    │       ├── open_webcam(source)
# #    │       ├── read()
# #    │       ├── detect(frame)
# #    │       └── get_boxes(results)
# #    │
# #    ├── Drawer
# #    │       |
# #    │       └── draw(
# #    │             annotated_frame,
# #    │             x1,
# #    │             y1,
# #    │             x2,
# #    │             y2,
# #    │             label,
# #    │             confidence
# #    │          )
# #    │
# #    └── Video_Saver
# #            |
# #            ├── create_writer()
# #            ├── write_frame(frame)
# #            └── release()


# def main():
#     args=get_args()
#     if args.task == "detect":
#         print("Source from argparse:", args.source)
#         d2=Detection(args.model,args.conf,args.source)
#         d2.open_webcam(args.source)
#         r2=Drawer()
#         v2=Video_Saver("Output",args.save_dir,d2.cap)
#         v2.create_writer()
#         while True:

#          ret, frame = d2.read()

#          if not ret:
#           print("Frame not received")
#          break

#         results = d2.detect(frame)

#         boxes = d2.get_boxes(results)

#         annotated_frame = frame.copy()

#         for box in boxes:

#           annotated_frame = r2.draw(
#             annotated_frame,
#             box["x1"],
#             box["y1"],
#             box["x2"],
#             box["y2"],
#             box["label"],
#             box["conf"]
#         )

#     # show camera window
#         cv2.imshow("Detection", annotated_frame)

#     # save video
#         v2.write_frame(annotated_frame)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#          break
#     # press q to exit


# # release resources
#         d2.release()
#         v2.release()
#         cv2.destroyAllWindows()
from Scripts.detect import  Detection
from Scripts.drawer import  Drawer
from Scripts.save_video import  Video_Saver
import cv2
from Utils.args import get_args
def main():
    args = get_args()

    if args.task == "detect":
        print("Source from argparse:", args.source)

        d2 = Detection(args.model, args.conf, args.source)
        d2.open_webcam(args.source)

        r2 = Drawer()

        v2 = Video_Saver("Output", args.save_dir, d2.cap)
        v2.create_writer()

        while True:

            ret, frame = d2.read()

            if not ret:
                print("Frame not received")
                break

            results = d2.detect(frame)

            boxes = d2.get_boxes(results)
            boxes = d2.get_boxes(results)
            print("Detections found:", len(boxes))

            annotated_frame = frame.copy()

            for box in boxes:

                annotated_frame = r2.draw(
                    annotated_frame,
                    box["x1"],
                    box["y1"],
                    box["x2"],
                    box["y2"],
                    box["label"],
                    box["conf"]
                )

            # show camera
            cv2.imshow("Detection", annotated_frame)

            # save video
            v2.write_frame(annotated_frame)

            # exit with q
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break


        # release after loop
        d2.release()
        v2.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()