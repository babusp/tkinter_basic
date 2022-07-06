from tkinter import *

maswin=Tk()
maswin.title("Master: Entry windows ")
maswin.geometry('600x300')
#lable
lbl=Label(maswin,text="User Name",bg="red",fg="yellow")

#pack
#lbl.pack()

#grid
#lbl.grid()


#-->inp--> place
lbl.place(x=150,y=140)


maswin.mainloop()

