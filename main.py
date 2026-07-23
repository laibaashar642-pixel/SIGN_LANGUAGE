# args.py
#   |
#   ↓
# main.py
#   |
#   ├── Camera 
#   ├── Detection 
#   ├── Drawer 
#   └── Video_Saver 
from Scripts.detect import  Detection
from Scripts.drawer import  Drawer
from Scripts.save_video import  Video_Saver

from Utils.args import get_args


def main():
    args=get_args()
    if args.task == "detect":
        print("Source from argparse:", args.source)
       
        d2=Detection(args.model,args.conf,args.source)
        d2.open_webcam(args.source)
        r2=Drawer()
        v2=Video_Saver("Output",args.save_dir,d2.cap)
if __name__ == "__main__":
    main()
