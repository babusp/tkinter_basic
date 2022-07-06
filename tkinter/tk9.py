from tkinter import *

maswin=Tk()
maswin.title("Master: Entry windows ")
maswin.geometry('600x300')

#lable
lbl=Label(maswin,text="User Name",bg="red",fg="yellow")
lbl.place(x=30,y=50)
#entry
ent=Entry(maswin,bg="yellow",fg="red",bd=5)
ent.place(x=110,y=50)


#button




maswin.mainloop()

