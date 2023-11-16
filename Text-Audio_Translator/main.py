from gtts import gTTS
import os

f=open("Sample.txt")
x=f.read()

langauge='en'

audio=gTTS(text=x,slow=False)
audio.save("audio.wav")
os.system("audio.wav")
