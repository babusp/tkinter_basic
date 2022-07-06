from tkinter import *
from tkinter import messagebox
top = Tk()
C = Canvas(top, height=600, width=400)
filename = PhotoImage(file = "./ball.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
btn=Button(top,text="sumbit").pack()
top.mainloop()