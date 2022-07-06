# from tkinter import *
# shan=Tk()
# # add widgets here

# shan.title('Hello Python')
# shan.geometry("300x200+10+20")
# shan.mainloop()


from tkinter import*
import tkinter as tk
window=Tk()
btn=Button(window, text="This is Button widget", fg='blue')
btn.place(x=10, y=10)
window.iconbitmap("work.ico")
window.title('Hello Python')
window.geometry("300x600+10+10")
# window.mainloop()
#---------------
#Lbl=Label(window,text="username")
# name_label = Label(window, text = 'Username', font=('calibre',10, 'bold'))
# name_label.grid(row=5,column=15)
# Lbl = Label(window, text="User Name",fg="red",bg="black")

# Lbl.pack( side = LEFT)
# Ent = Entry(window, bd =15)
# Ent.pack(side = RIGHT)

# btn=Button(window, text="This is Button widget", fg='blue')
# btn.place(x=100, y=500)
# window.title('Hello Python')
# window.geometry("300x600")
window.mainloop()
