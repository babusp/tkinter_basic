from fileinput import close
from statistics import geometric_mean
from tkinter import *
import tkinter as tk
root = Tk()
root.geometry('500x600')
#root.configure(bg='yellow')
root.title("Blood Donation Form")
root.iconbitmap("blood.ico")


# class App():
#     def __init__(self):
#         self.label = tk.Label(text="DONATE BLOOD SAVE LIFE ",width=30,font=("bold", 20))
        
#         self.label.place(x=30, y=300)
#         self.label.after(1000, self.clear_label)    # 1000ms

#     def clear_label(self):
#         print ("clear_label")
#         self.label.place_forget()

# app=App()

title=Label(root, text=" Donation Regestration Form",width=22,font=("bold", 20)).place(x=90,y=30)

name = Label(root, text="Full Name :",width=20,font=("bold", 10)).place(x=60,y=100)
name_entry = Entry(root).place(x=200,y=100)

father=Label(root, text="Father's Name :",width=20,font=("bold", 10)).place(x=60,y=150)
father_entry = Entry(root).place(x=200,y=150)

var_gender=IntVar()
gender=Label(root, text="Gender :",width=20,font=("bold", 10)).place(x=60,y=200)
Radiobutton(root, text="Male",padx = 5, variable=var_gender, value=1).place(x=200,y=200)
Radiobutton(root, text="Female",padx = 20, variable=var_gender, value=2).place(x=275,y=200)

dob=Label(root, text="Date Of Birth :",width=20,font=("bold", 10)).place(x=60,y=250)
entry_dob=Entry(root,).place(x=200,y=250)

email= Label(root, text="Email-id :",width=20,font=("bold", 10)).place(x=60,y=300)
email_entry = Entry(root).place(x=200,y=300)

phone= Label(root, text="Mobile No :",width=20,font=("bold", 10)).place(x=60,y=350)
phone_entry = Entry(root).place(x=200,y=350)

addrs= Label(root, text="Address :",width=20,font=("bold", 10)).place(x=60,y=400)
entry_addr=Entry(root).place(x=200,y=400)

var_blood=IntVar()
var_blood.set("selct blood type")
blood=Label(root, text="Blood Type :",width=20,font=("bold", 10)).place(x=60,y=450)
b_type=OptionMenu(root, var_blood, "A RhD positive (A+)","A RhD negative (A-)" ,"B RhD positive (B+)", "B RhD negative (B-)",
            "O RhD positive (O+)","O RhD negative (0-)","AB RhD positive (AB+)","AB RhD negative (AB-)").place(x=200,y=450)

var_test=IntVar()
test=Label(root, text="Is Test are done :",width=20,font=("bold", 10)).place(x=60,y=500)
Radiobutton(root,text="Yes",value=1,variable=var_test).place(x=200,y=500)
Radiobutton(root,text="No",value=2,variable=var_test).place(x=275,y=500)

#if var_test.get()!=1:
#     test=Label(root, text="please contact managemnet",width=20,font=("bold", 10)).place(x=60,y=550)
# else:
#     test_id=Label(root,text="enter test id :",width=20,font=("bold", 10)).place(x=60,y=550)
#     entry_test=Entry(root).place(x=200,y=550)

def data():
    dt=Tk()
    dt.geometry('200x100')
    info=Label(dt,text="info saved successfully").place(x=30,y=30)
    def close():
        dt.destroy()
        root.destroy()


    ok_btn=Button(dt,text="ok",command=close).place(x=100,y=50)
    dt.mainloop()

btn=Button(root, text="SUMBIT",command=data,fg='blue').place(x=200, y=550)
root.mainloop()