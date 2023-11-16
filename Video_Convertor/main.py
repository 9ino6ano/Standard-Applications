from moviepy.editor import *

#insert the video file
clip=(VideoFileClip("thief.mp4").subclip(0.3))

#isnert gif file path
clip.write_gif("mygif.gif")