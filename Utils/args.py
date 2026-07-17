import argparse
def get_args():
    
      parser=argparse.ArgumentParser(description="CV Pipeline")
      parser.add_argument(
        "--task",
        type=str,
        required=True,
        choices=["detect"],
    )

      parser.add_argument(
          "--model",
        required=True)
      parser.add_argument(
          "--source", 
          required=True)
      parser.add_argument(
          "--project", 
          required=True)
      parser.add_argument(
        "--save-dir", 
        required=True, 
        dest="save_dir")
      parser.add_argument(
          "--conf",
            type=float,
            default=0.5)
      return parser.parse_args()