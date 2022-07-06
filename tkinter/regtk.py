from tkinter import *
root = Tk()
root.geometry('500x500')
#root.configure(bg='yellow')
root.title("Registration Form")
#root.iconbitmap("work.ico")



# C = Canvas(root, bg="blue", height=250, width=300)
# filename = PhotoImage(file = "ball.png")
# background_label = Label(root, image=filename)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
# C.pack()


label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Fullname",width=15,font=("bold", 10))
label_1.place(x=60,y=100)

entry_1 = Entry(root)
entry_1.place(x=200,y=100)

label_2= Label(root, text="Email",width=15,font=("bold", 10))
label_2.place(x=60,y=150)

entry_2 = Entry(root)
entry_2.place(x=200,y=150)

label_3= Label(root, text="Phone",width=15,font=("bold", 10))
label_3.place(x=60,y=200)

entry_3 = Entry(root)
entry_3.place(x=200,y=200)

label_4 = Label(root, text="Gender",width=15,font=("bold", 10))
label_4.place(x=60,y=250)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=200,y=250)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=275,y=250)

label_5= Label(root, text="Age",width=15,font=("bold", 10))
label_5.place(x=60,y=300)

entry_5 = Entry(root)
entry_5.place(x=200,y=300)

label_6= Label(root, text="Technologies",width=15,font=("bold", 10))
label_6.place(x=60,y=350)
Checkbutton1 = IntVar()  
Checkbutton2 = IntVar()  
Checkbutton3 = IntVar()
Checkbutton4 = IntVar()
Button1 = Checkbutton(root, text = "PYTHON",variable = Checkbutton1,onvalue=1).place(x=200,y=350)
Button2 = Checkbutton(root, text = "AWS & DEVOPS",variable = Checkbutton2,onvalue=2).place(x=275,y=350)
Button3 = Checkbutton(root, text = "LINUX",variable = Checkbutton3,onvalue=1).place(x=200,y=400)
Button4 = Checkbutton(root, text = "FULL STACK",variable = Checkbutton4,onvalue=1).place(x=275,y=400)
def my_func():
    a=[]
    if Checkbutton1.get()==1:
        chk1="PYTHON"
        a.append(chk1)
        print(chk1)
    if Checkbutton2.get()==1:
        chk2="AWS &DEVOPS"
        a.append(chk2)
        print(chk2)
    if Checkbutton3.get()==1:
        chk3="LINUX"
        a.append(chk3)
        print(chk3)

    if Checkbutton4.get()==1:
        chk4="FULL STACK"
        a.append(chk4)
        print(chk4)
    
    print(a)

        
    var.get()
    if var.get()==1:
        gen="male"
        print(gen)
    else:
        gen="female"
        print(gen)

btn=Button(root, text="SUMBIT",command=my_func,fg='blue').place(x=200, y=450)


root.mainloop()