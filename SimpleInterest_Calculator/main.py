from tkinter import *

root=Tk()
root.title("Simple Interest Calculator")
root.geometry("500x300")

def Calculate():
    prin=int(principalEntry.get())
    rat=int(rateEntry.get())
    tim=int(timeEntry.get())
    amount=(prin*rat*tim)/100
    Label(text=f'{amount}',font="arial 30 bold").place(x=200,y=220)


principal=Label(root,text="Principal:",font="arial 15")
rate=Label(root,text="Rate Of Interest:",font="arial 15")
time=Label(root,text="Duration:",font="arial 15")

principal.place(x=40,y=20)
rate.place(x=40,y=90)
time.place(x=40,y=160)

principalValue=StringVar()
rateValue=StringVar()
timeValue=StringVar()

principalEntry=Entry(root,textvariable=principalValue,font="arial 20",width=8)
rateEntry=Entry(root,textvariable=rateValue,font="arial 20",width=8)
timeEntry=Entry(root,textvariable=timeValue,font="arial 20",width=8)

principalEntry.place(x=200,y=20)
rateEntry.place(x=200,y=90)
timeEntry.place(x=200,y=160)

interest=Label(root,text="Interest: ",font="arial 15")
interest.place(x=50,y=230)

Button(text="Calculate",font="arial 15",command=Calculate).place(x=350,y=20)
Button(root,text="Exit",font="arial 15",width=8,command=exit).place(x=350,y=90)

root.mainloop()
"""
def Calculate():
    prin=int(principalEntry.get())
    rat=int(rateEntry.get())
    tim=int(timeEntry.get())
    amount=(prin*rat*tim)/100
    Label(text=f'{amount}',font="arial 30 bold").place(x=200,y=220)

principal=Label(root,text="Principal:",font="arial 15")
rate=Label(root,text="Rate Of Interest:",font="arial 15")
time=Label(root,text="Duration:",font="arial 15")

principal.place(x=50,y=20)
rate.place(x=50,y=90)
time.place(x=50,y=160)

interest=Label(root,text="Interest: ",font="arial 15")
interest.place(x=50,y=230)


principalValue=StringVar()
rateValue=StringVar()
timeValue=StringVar()

principalEntry=Entry(root,textvariable=principalValue,font="arial 20",width=8)
rateEntry=Entry(root,textvariable=rateValue,font="arial 20",width=8)
timeEntry=Entry(root,textvariable=timeValue,font="arial 20",width=8)


principalEntry.place(x=200,y=20)
rateEntry.place(x=200,y=90)
timeEntry.place(x=200,y=160)


Button(text="Calculate",font="arial 15",command=Calculate).place(x=350,y=20)
Button(text="Exit",command=exit(),font="arial 15",width=8).place(x=350,y=90)


root.mainloop()

"""