import tkinter
from tkinter import *

root=Tk()
root.title("Grade Calculator")
root.geometry("500x400")


def Calculation():
    english=int(englishEntry.get())
    skills=int(analytical_skillEntry.get())
    general=int(generalEntry.get())
    total_marks=(english+skills+general)
    Label(text=f'{total_marks}',font="arial 15 bold").place(x=250,y=170)


    average_marks=int(total_marks/3)
    Label(text=f"{average_marks}",font="arial 15 bold").place(x=250,y=210)


    if (average_marks > 50):
        grade="PASS"
    else:
        grade="FAIL"

    Label(text=f'{grade}',font="arial 15 bold",fg="blue").place(x=250,y=250)


#Subject
sub1=Label(root,text="English:",font="arial 10")
sub2=Label(root,text="Analytical Skill:",font="arial 10")
sub3=Label(root,text="General Knowledge:",font="arial 10")
total=Label(root,text="Total:",font="arial 10")
avg=Label(root,text="Average:",font="arial 10")
grade=Label(root,text="Grade:",font="arial 10")

sub1.place(x=50,y=20)
sub2.place(x=50,y=70)
sub3.place(x=50,y=120)
total.place(x=50,y=170)
avg.place(x=50,y=210)
grade.place(x=50,y=250)

englishValue=StringVar()
analytical_skillValue=StringVar()
general_Value=StringVar()

englishEntry=Entry(root,textvariable=englishValue,font="arial 15",width=15)
analytical_skillEntry=Entry(root,textvariable=analytical_skillValue,font="arial 15",width=15)
generalEntry=Entry(root,textvariable=general_Value,font="arial 15",width=15)

englishEntry.place(x=250,y=20)
analytical_skillEntry.place(x=250,y=70)
generalEntry.place(x=250,y=120)


Button(text="Calculate",font="arial 15",bg="white",bd=10,command=Calculation).place(x=50,y=300)
Button(text="Exit",font="arial 15", bg="white",bd=10,width=8,command=lambda:exit()).place(x=350,y=300)


root.mainloop()