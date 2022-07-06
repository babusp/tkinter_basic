from tkinter import *
from tkinter import ttk

maswin=Tk()
maswin.title("Master")
#maswin.iconbitmap('icon.ico')
maswin.maxsize(width=600,height=300)
maswin.minsize(width=600,height=300)

def func():
   if var.get()==0:
      print("Male")
   else:
      print("Female")


var=IntVar()
rd=Radiobutton(maswin,text="Male",value=0,variable=var).pack()
rd=Radiobutton(maswin,text="Female",value=1,variable=var).pack()

btn=Button(maswin,text="Submeet",command=func).pack()


maswin.mainloop()

