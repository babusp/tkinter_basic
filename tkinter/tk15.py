from tkinter import *
from tkinter import ttk

maswin=Tk()
maswin.title("Master")
#maswin.iconbitmap('icon.ico')
maswin.maxsize(width=600,height=300)
maswin.minsize(width=600,height=300)

def func():
    print(chkbtn1.get())
    print(chkbtn2.get())


chkbtn1=IntVar()
chkbtn2=IntVar()

cho=Checkbutton(maswin,text="Male",variable=chkbtn1,onvalue=1,offvalue=0)
cho.pack()

cho=Checkbutton(maswin,text="Female",variable=chkbtn2,onvalue=1,offvalue=0)
cho.pack()


maswin.mainloop()

