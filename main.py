
import argparse
from Utils.args import get_args
from Weights.Scripts.detect import  Detection


def main():
    args=get_args()
    if args.task == "detect":
        print("Source from argparse:", args.source)
        d2=Detection(model_path=args.model,conf=args.conf)#Object creation to use the class of detection
        d2.language_detection( #utilizing the function method by calling it 
        source=args.source,
        project=args.project,
        save_dir=args.save_dir,
        )

if __name__ == "__main__":
    main()
