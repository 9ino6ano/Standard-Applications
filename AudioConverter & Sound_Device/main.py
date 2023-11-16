#python code to convert video to audio
import moviepy.editor as mp

#insert the video file
clip = mp.VideoFileClip(r"40 Days40 Nights.mp4")

#insert audio file path
clip.audio.write_audiofile(r"40 Days40 Nights.wav")

