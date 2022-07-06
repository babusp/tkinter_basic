
import tkinter as tk
from tkinter import ttk
import MySQLdb as mdb
 
 
class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
 
        self.title("Geekscoders - DB Connection")
        self.minsize(300,250)
        self.iconphoto(False, tk.PhotoImage(file='geekscoders.png'))
 
        self.label_frame = ttk.LabelFrame(self, text = "Database Connection")
        self.label_frame.grid(column = 0, row  =0, padx = 20, pady = 20)
 
        self.create_widgets()
 
 
 
 
    def create_widgets(self):
        button = ttk.Button(self.label_frame, text = "Connection Status", command = self.db_connect)
        button.grid(column = 0, row = 0)
 
        self.label = ttk.Label(self.label_frame, text = "")
        self.label.grid(column = 0, row = 1)
 
 
 
    def db_connect(self):
        try:
            db = mdb.connect('localhost', 'root', '', 'tkdb')
            self.label.configure(text = "Connected Successfully")
 
 
        except mdb.Error as e:
            self.label.configure(text = "Not Successfully Connected")
 
 
 
 
window = Window()
window.mainloop()