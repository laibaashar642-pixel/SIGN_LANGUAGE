from moviepy import VideoFileClip

clip = VideoFileClip("Demo/Output.mp4")
clip = clip.subclipped(0, 8)
clip = clip.resized(width=480)
clip.write_gif("Demo/demo.gif", fps=10)