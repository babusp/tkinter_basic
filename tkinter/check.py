from tkinter import *
root = Tk()
root.geometry('500x800')
#root.configure(bg='yellow')
root.title("Registration Form")
root.iconbitmap("work.ico")

C = Canvas(root,height=250, width=300)
filename = PhotoImage(file = "./ball.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="FullName",width=15,font=("bold", 10))
label_1.place(x=60,y=100)

entry_1 = Entry(root)
entry_1.place(x=200,y=100)

label_2= Label(root, text="Email",width=15,font=("bold", 10))
label_2.place(x=60,y=150)

entry_2 = Entry(root)
entry_2.place(x=200,y=150)

u_str=StringVar()
label_3= Label(root, text="User Name",width=15,font=("bold", 10))
label_3.place(x=60,y=200)
entry_3 = Entry(root,textvariable=u_str).place(x=200,y=200)

label_4 = Label(root, text="Gender",width=15,font=("bold", 10))
label_4.place(x=60,y=250)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=200,y=250)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=275,y=250)

p_str = StringVar()
label_5= Label(root, text="Password",width=15,font=("bold", 10))
label_5.place(x=60,y=300)

entry_5 = Entry(root,textvariable=p_str, show='*')
entry_5.place(x=200,y=300)

r_str=StringVar()
label_6= Label(root, text="Re-enter Password",width=15,font=("bold", 10)).place(x=60,y=350)
entry_6 = Entry(root,textvariable=r_str, show='*').place(x=200,y=350)

def my_func():
    
    if p_str.get()==r_str.get():
        label_7=Label(root,text="Registation Successfull,login agian",width=40,font=("bold", 10)).place(x=40,y=450)
        login()
    else:
        label_8=Label(root,text="Password Not Matched",width=40,font=("bold", 10)).place(x=40,y=450)


btn=Button(root, text="SUMBIT",command=my_func,fg='blue').place(x=200, y=400)

def login():
    log=Tk()
    log.geometry("400x400")
    
    u_login=Label(log,text="login",width=20,font=("bold", 20)).place (x=50,y=50)

    l_str=StringVar()
    label_9= Label(log, text="User Name",width=15,font=("bold", 10)).place(x=60,y=100)
    entry_9= Entry(log,textvariable=l_str).place(x=200,y=100)
    l_p_str=StringVar()
    label_10= Label(log,text="Password",width=15,font=("bold", 10)).place(x=60,y=150)
    entry_10 = Entry(log,textvariable=l_p_str, show='*').place(x=200,y=150)
    def signin():
        if u_str.get()==l_str.get():
            if p_str.get()==l_p_str.get():
                label_11=Label(log,text="login Successfull",widt=40,font=("bold", 10)).place(x=40,y=250)
            else:
                label_12=Label(log,text="Password Wrong",width=40,font=("bold", 10)).place(x=40,y=250)
        else:
            label_13=Label(log,text="Username Wrong",width=40,font=("bold", 10)).place(x=40,y=250)
    login_btn=Button(log, text="Sign-in",command=signin,fg='blue').place(x=200, y=200)
    quit = Button(log, text="quit", command=log.destroy).place(x=400,y=300)
    log.mainloop()
root.mainloop()

root.mainloop()