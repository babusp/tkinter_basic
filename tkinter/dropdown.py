from cProfile import label
from tkinter import *
from turtle import width
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
#from crc.input import team_A,team_B
#team_A,team_B =StringVar()#="hyd","bng"
master = Tk()
master.geometry("600x600")

my_dict={1:'Jan',2:'Feb',3:'March',4:'April',5:'May'}
months=list(my_dict.values())
sel=tk.StringVar() # string variable for the Combobox
font1=('Times',18,'normal')
cb1=ttk.Combobox(my_w,values=months,width=7,
    textvariable=sel,font=font1)
cb1.grid(row=1,column=1,padx=10, pady=20)    


btn=Button(master, text="SUMBIT",fg='blue').place(x=200, y=550)
master.mainloop()




