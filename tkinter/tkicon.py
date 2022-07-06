from tkinter import *
root = Tk()
root.geometry('500x500')
root.title("Registration Form")
root.iconbitmap("work.ico")

label_0 = Label(root, text="FEEDBACK FORM",width=20,font=("bold", 20),fg="red",bg="black")
label_0.place(x=90,y=30)

label_1 = Label(root, text="Topic",width=10,font=("bold", 10),fg="red",bg="black")
label_1.place(x=60,y=100)

entry_1 = Entry(root,fg="red")
entry_1.place(x=200,y=100)

label_2 = Label(root, text="Trainer Name",width=10,font=("bold", 10),fg="red",bg="black")
label_2.place(x=60,y=150)

entry_2 = Entry(root,fg="red")
entry_2.place(x=200,y=150)

label_3 = Label(root, text="Feedback",width=10,font=("bold", 10),fg="red",bg="black")
label_3.place(x=60,y=200)
#drop down
variable = StringVar(root)
variable.set("-----") # default value
drop= OptionMenu(root, variable, "Not Good ", "Good", "Aewsome")
drop.place(x=200,y=200)

# Checkbutton1 = IntVar()  
# Checkbutton2 = IntVar()  
# Checkbutton3 = IntVar()
# Checkbutton4 = IntVar()
# Button1 = Checkbutton(root, text = "Worst ",variable = Checkbutton1,onvalue=1,fg="black").place(x=200,y=200)
# Button2 = Checkbutton(root, text = "Not Good",variable = Checkbutton2,onvalue=1,fg="red").place(x=275,y=200)
# Button3 = Checkbutton(root, text = "Good",variable = Checkbutton3,onvalue=1,fg="blue").place(x=200,y=250)
# Button4 = Checkbutton(root, text = "Aewsome",variable = Checkbutton4,onvalue=1,fg="green").place(x=275,y=250)

root.mainloop()