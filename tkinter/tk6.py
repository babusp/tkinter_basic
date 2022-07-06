from tkinter import *

maswin=Tk()
maswin.title("Master: Entry windows ")
maswin.geometry('600x300')
#lable
lbl=Label(maswin,text="User Name")

#pack
#lbl.pack()

#grid
#lbl.grid()
lbl.grid(row=20,column=20)

#place


maswin.mainloop()

