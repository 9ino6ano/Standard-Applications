from tkinter import *
from tkinter import messagebox
import sounddevice
from scipy.io.wavfile import write
import time
import wavio as wv
#make sure you have installed all the necessary modules e.g sounddevice, wavio,scipy

root=Tk()
root.geometry("600x700+400+80")
root.resizable(False,False)
root.title("Voice Recorder")
root.configure(background="#4a4a4a")


#the function for recording the sound
def record():
    freq=44100
    dur=int(duration.get())
    recording=sounddevice.rec(dur*freq,samplerate=freq,channels=2)
    #include a time down
    try:
        temp=int(duration.get())
    except:
        print("Please enter the correct value")
    while temp>0:
        root.update()
        time.sleep(1)
        temp-=1

        if (temp == 0):
            messagebox.showinfo("Countdown Timer","Time is up!!!")
        Label(text=f'{str(temp)}',font='arial 40',width=4,background="#4a4a4a").place(x=240,y=590)

    sounddevice.wait()
    write("recording.wav",freq,recording)


#icon
image_icon=PhotoImage(file="Record.png")
root.iconphoto(False,image_icon)
#logo
photo=PhotoImage(file="Record.png")
myImage=Label(image=photo,background="#4a4a4a")
myImage.pack(padx=5,pady=5)

#name
Label(text="Voice Recorder",font="arial 30 bold",background="#4a4a4a",fg="white").pack()

#entry box
duration = StringVar()
entry = Entry(root,textvariable=duration,font="arial 30",width=15).pack(pady=10)
Label(text="Enter the (Rec) time in seconds...",font="arial 15",background="#4a4a4a",fg="white").pack()

#button
record=Button(root,font="arial 20",text="Record",bg="#111111",fg="white",border=0,command=record).pack(pady=30)


root.mainloop()