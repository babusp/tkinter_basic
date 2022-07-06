from tkinter import *
from tkinter import ttk

maswin=Tk()
maswin.title("Master")
#maswin.iconbitmap('icon.ico')
maswin.maxsize(width=600,height=300)
maswin.minsize(width=600,height=300)

var=StringVar()

com=ttk.Combobox(maswin,width=27)
com['state']='readonly'
com['values']=('Jan','Feb','Mar','Apr')
com.place(x=100,y=10)
com.current(0)

maswin.mainloop()

