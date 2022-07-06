
from tkinter import *
root = Tk()
root.geometry('600x600')
#root.configure(bg='yellow')
root.title("Registration Form")
root.iconbitmap("work.ico")

# from datetime import datetime as dt
# now = dt.now()
# today = now.strftime("%Y/%m/%d")
# s='2022/2/20'
# res = (dt.strptime(today, "%Y/%m/%d") - dt.strptime(s, "%Y/%m/%d")).days
# print(res)

def create():
    root1=Tk()
    root1.geometry('600x400')
    #root1.configure(bg='yellow')
    root1.title("Registration Form")

    m_id=Label(root1,text="Match_id :",width=10,font=("bold", 10)).place(x=60,y=100)
    entry_m_id=Entry(root1).place(x=200,y=100)

    def success_info():
        root2=Tk()
        root2.geometry('200x200')
       # root2.configure(bg='yel')
        root2.title("info")
        info=Label(root1,text="details saved successfully",width=10,font=("bold", 10)).place(x=60,y=100)
        ok_btn=Button(root,text="Create Match",command=success_info).place(x=100,y=150)
        root2.mainloop()
        
    save_btn=Button(root1,text="save",command=success_info).place(x=200,y=300)

    # venue=Label(root,text="Venue :",width=20,font=("bold", 10)).place(x=60,y=150)
    # entry_venue=Entry(root).place(x=200,y=150)

    # dt=Label(root,text="Date :",width=20,font=("bold", 10)).place(x=60,y=200)
    # entry_dt=Entry(root).place(x=200,y=200)

    # time=Label(root,text="Time :",width=20,font=("bold", 10)).place(x=60,y=250)
    # entry_time=Entry(root).place(x=200,y=250)


 
    

    root1.mainloop()



 

create_btn=Button(root,text="Create Match",command=create).place(x=60,y=60)






root.mainloop()