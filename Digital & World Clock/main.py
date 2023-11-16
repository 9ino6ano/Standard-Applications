from tkinter import *
from tkinter.ttk import *
from time import strftime

top=Tk()
top.title("Digital Clock")
def none():
    text=strftime(' %H:%M:%SS %p ')
    lbl.config(text=text)
    lbl.after(1000,none)


lbl=Label(top,font=('digital-7' ,50,'bold'),
           background='darkgrey',foreground='cyan')
lbl.pack(anchor='center')
none()
mainloop()