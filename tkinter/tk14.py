from multiprocessing.sharedctypes import Value
from optparse import Values
from tkinter import *
from tkinter import ttk

maswin=Tk()
maswin.title("Master")
#maswin.iconbitmap('icon.ico')
maswin.maxsize(width=600,height=300)
maswin.minsize(width=600,height=300)

chkbtn=IntVar()

cho=Radiobutton(maswin,text="Male", variable=chkbtn,value=1)
cho.pack()

cho=Radiobutton(maswin,text="Female",variable=chkbtn,value =2)
cho.pack()


maswin.mainloop()

