from tkinter import *

maswin=Tk()
maswin.title("Master: Entry windows ")
maswin.geometry('600x300')

#func
def myfunc():
  x=var.get()
  lbl.config(text=x)


#lable
lbl=Label(maswin,text="User Name",bg="red",fg="yellow")
lbl.place(x=30,y=50)

#entry
var=StringVar()
ent=Entry(maswin,bg="yellow",fg="red",bd=5,textvariable=var)
ent.place(x=110,y=50)


#button
btn=Button(maswin,text="Next",command=myfunc)
btn.place(x=100,y=150)






maswin.mainloop()

