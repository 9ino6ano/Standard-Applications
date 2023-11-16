import ast
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)
#################################
def signup():
    window=Toplevel(root)
    window.title("Sign-Up")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False, False)

    # function for sign up
    def signup():
        username = user.get()
        password = code.get()
        conf_passw = confirm_pass.get()

        if password == conf_passw:
            try:
                file = open('datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)
                dict2 = {username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open('datasheet.txt', 'w')
                w = file.write(str(r))

                messagebox.showinfo('Sign-Up', f'{username}, Successfully signed up!!')
                window.destroy()
            except:
                file = open('datasheet.txt', 'w')
                pp = str({'username': 'password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid Info', 'The Username and Password should Match!!')

    def sign():
        window.destroy()

    img = PhotoImage(file="login.png")
    Label(window, image=img, border=0, bg="white").place(x=50, y=90)
    frame = Frame(window, width=350, height=390, bg="#fff")
    frame.place(x=400, y=50)

    heading = Label(frame, text='Sign-Up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    ##########
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", on_enter)
    user.bind("FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    ##########
    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        if code.get() == '':
            code.insert(0, 'Password')

    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", on_enter)
    code.bind("FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    ##########
    def on_enter(e):
        confirm_pass.delete(0, 'end')

    def on_leave(e):
        if confirm_pass.get() == '':
            confirm_pass.insert(0, 'Confirm Password')

    confirm_pass = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    confirm_pass.place(x=30, y=220)
    confirm_pass.insert(0, 'Confirm Password')
    confirm_pass.bind("<FocusIn>", on_enter)
    confirm_pass.bind("FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    ##################
    Button(frame, width=39, pady=7, text='Sign-Up', bg="#57a1f8", fg='white', border=0, command=signup).place(x=35,
                                                                                                              y=280)
    label = Label(frame, text='I already have an account?', fg='black', bg='white',
                  font=('Microsoft Yahei UI Light', 9))
    label.place(x=90, y=340)

    sign_in = Button(frame, width=6, text='Sign-in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign)
    sign_in.place(x=200, y=340)

    window.mainloop()

################################################
#If you combine these forms, then you can create 2 seperate windows using a single form, each with different call events.
def sign_up():
    username=user.get()
    passw=password.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    print(r.keys())
    print(r.values())
#if username in r.keys() and password==r[username]:
#else: messagebox.showerror('Invalid Input','The input was inserted incorrectly')

    if username=="" and passw=="":
        print("Blank Selection")
        messagebox.showinfo("Empty Selection",'Please Input Your Information On The Fields Provided')
        return

    elif username=="admin-man"and passw=="admin@123":
        print("Welcome Administrator")
        screen=Toplevel(root)
        screen.title("Application")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')
        Label(screen,text='Management-9ino6ano Academy',bg="#fff",font=('Microsoft Yahei UI Light',50,'bold')).pack(expand=True)
        screen.mainloop()


    elif username=="st-guest"and passw=="st123":
        print('Welcome Guest')
        screen = Toplevel(root)
        screen.title("Application")
        screen.geometry('925x500+300+200')
        screen.config(bg='lightgrey')
        Label(screen, text='Welcome To 9ino6ano Academy', bg="#fff",font=('Calibri(Body)',50,'bold')).pack(expand=True)
        screen.mainloop()
    else:
        messagebox.showerror("Invalid Input","The Username or Password is incorrect")
        return


img=PhotoImage(file='login2.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)
#_______________________________________________________________
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind("<FocusIn>",on_enter)
user.bind("FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
#________________________________________________________________
def on_enter(e):
    password.delete(0,'end')

def on_leave(e):
    if password.get()=='':
        password.insert(0,'Username')


password = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
password.place(x=30,y=150)
password.insert(0,'Password')
password.bind("<FocusIn>",on_enter)
password.bind("FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
#________________________________________________________________
Button(frame,width=39,pady=7,text='Log in',bg='#57a1f8',fg='white',border=0,command=sign_up).place(x=35,y=204)
label=Label(frame,text="I don't have an account?",fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign-Up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup)
sign_up.place(x=215,y=270)




root.mainloop()