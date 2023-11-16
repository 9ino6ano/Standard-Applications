from tkinter import *
import os

root=Tk()
root.title("Shutdown App")
root.geometry("400x580")

def restart_time():
    os.system("shutdown /r /t 30")

def restart():
    os.system("shutdown /r /t 1")

def shutdown():
    os.system("shutdown /s /t 1")

def logout():
    os.system("shutdown -l")

#1st button
restart_time_button=PhotoImage(file="ProjectImages/restart time.png")
first_button=Button(root,image=restart_time_button,borderwidth=0,cursor="hand2",command=restart_time)
first_button.place(x=10,y=10)

#second button
close_button=PhotoImage(file="ProjectImages/close.png")

second_button=Button(root,image=close_button,borderwidth=0,cursor="hand2",command=root.destroy)
second_button.place(x=200,y=10)

#third button
restart_button=PhotoImage(file="ProjectImages/restart.png")

third_button=Button(root,image=restart_button,borderwidth=0,cursor="hand2",command=restart)
third_button.place(x=10,y=200)

#fourth button
shutdown_button=PhotoImage(file="ProjectImages/shutdown.png")

fourth_button=Button(root,image=shutdown_button,borderwidth=0,cursor="hand2",command=shutdown)
fourth_button.place(x=200,y=200)

#fifth button
logout_button=PhotoImage(file="ProjectImages/log out.png")

fifth_button=Button(root,image=logout_button,borderwidth=0,cursor="hand2",command=logout)
fifth_button.place(x=10,y=400)





root.mainloop()