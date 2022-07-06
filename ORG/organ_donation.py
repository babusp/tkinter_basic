#from distutils.log import Log
from email.mime import image
from msilib.schema import ComboBox
from multiprocessing.sharedctypes import Value
from tkinter import *
import tkinter as tk
import time
import mysql.connector as mc

root=Tk()
root.geometry("1500x800")
root.configure(bg="white")

# C = Canvas(root)#, bg="blue", height=250, width=300)
# filename1 = PhotoImage(file = "donp.png")
#background_label = Label(root, image=filename).place(x=510, y=100)
#C.pack()


outerframe = Frame(root, bd=12, relief=RIDGE, padx=20, bg="red").place(x=0, y=0, width=1500, height=1300)
frame1 = Frame(root, bd=12, relief=RIDGE, padx=20, bg="powder blue").place(x=10, y=10, width=500, height=1250)
frame2 = Frame(root, bd=12, relief=RIDGE, padx=20, bg="white").place(x=500, y=10, width=990, height=1250)
frame3=Frame(root, bd=12, relief=RIDGE, padx=20, bg="white").place(x=510, y=100, width=980, height=680)


doc_image = Canvas(root)#, bg="blue", height=250, width=300)
filename2 = PhotoImage(file = "doc.png")
background_label = Label(root, image=filename2).place(x=520, y=25)

admin_image = Canvas(root)#, bg="blue", height=250, width=300)
filename3 = PhotoImage(file = "admin.png")
background_label = Label(root, image=filename3).place(x=1425, y=25)

def not_fill():
    info=Tk()
    info.geometry("200x100")
    info.configure(bg='grey')
    info_save=Label(info,text="---Must Fill All Fields---").place(x=30,y=30)
    ###Information Save repsonse window closed
    def close():
        info.destroy()
    ok_btn=Button(info,text="ok",command=close).place(x=80,y=65)
    info.mainloop()
        


## Information Save repsonse window
def login_error():
    info=Tk()
    info.geometry("200x100")
    info.configure(bg='grey')
    info_save=Label(info,text="---Wrong Credentials---").place(x=30,y=30)
    ###Information Save repsonse window closed
    def close():
        info.destroy()
    ok_btn=Button(info,text="ok",command=close).place(x=80,y=65)
    info.mainloop()

def save_donor():

    print(name_d.get())
    print(var_blood.get())
    a=''
    
    if heart_check.get()==1:
        h="heart,"
        a=a+h
    
    if lungs_check.get()==1:
        l="lungs,"
        a=a+l
    if liver_check.get()==1:
        lv="liver,"
        a=a+lv
    if kidney_check.get()==1:
        k="kidney"
        a=a+k
    org=a
    print(org)
    if var.get()==0:
        gen="Female"
    else:
        gen="Male"
    print(gen)

    if name_d.get()!="" and father_d.get()!="" and gen!="" and dob_d.get()!="" and email_d.get()!="" and phone_d.get()!="" and addr_d.get()!="" and var_blood.get()!="" and org!="" :
        mydb = mc.connect(host="localhost",user="root",password="shan",database="donate")
        mycursor = mydb.cursor()
        mycursor.execute("use donate")
        print(name_d.get(),father_d.get(),gen,dob_d.get(),email_d.get(),phone_d.get(),addr_d.get(),var_blood.get(),org)
        mycursor.execute("""INSERT INTO save_donor (Fullname,FatherName,Gender,DOB,Email,Mobile,Address,B_type,Organs) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""", 
                    (name_d.get(),father_d.get(),gen,dob_d.get(),email_d.get(),phone_d.get(),addr_d.get(),var_blood.get(),org))
        mydb.commit()
    else:
        not_fill()
    

title=Label(root, text=" Donor Regestration Form",width=22,bg="powder blue",font=("bold", 20)).place(x=90,y=30)
 
name_d=StringVar()
name = Label(root, text="Full Name :",width=15,bg="powder blue",font=("bold", 12)).place(x=60,y=100)
name_entry = Entry(root,textvariable=name_d,font=12).place(x=200,y=100)

father_d=StringVar()
father=Label(root, text="Father's Name :",width=15,bg="powder blue",font=("bold", 12)).place(x=60,y=150)
father_entry = Entry(root,textvariable=father_d,font=12).place(x=200,y=150)


var=IntVar()
gender=Label(root, text="Gender :",width=15,bg="powder blue",font=("bold", 12)).place(x=60,y=200)
Radiobutton(root, text="Male",padx = 5,bg="powder blue", variable=var, value=1,font=12).place(x=200,y=200)
Radiobutton(root, text="Female",padx = 20,bg="powder blue", variable=var, value=0,font=12).place(x=275,y=200)

dob_d=StringVar()
dob=Label(root, text="Date Of Birth :",width=15,bg="powder blue",font=("bold", 12)).place(x=60,y=250)
entry_dob=Entry(root,textvariable=dob_d,font=12).place(x=200,y=250)

email_d=StringVar()
email= Label(root, text="Email-id :",width=15,bg="powder blue",font=("bold", 12)).place(x=60,y=300)
email_entry = Entry(root,textvariable=email_d,font=12).place(x=200,y=300)

phone_d=StringVar()
phone= Label(root, text="Mobile No :",width=15,bg="powder blue",font=("bold", 12)).place(x=60,y=350)
phone_entry = Entry(root,textvariable=phone_d,font=12).place(x=200,y=350)

addr_d=StringVar()
addrs= Label(root, text="Address :",width=15,bg="powder blue",font=("bold", 12)).place(x=60,y=400)
entry_addr=Entry(root,textvariable=addr_d,font=12).place(x=200,y=400)

var_blood=StringVar()
b_types={1:"A RhD positive (A+)",2:"A RhD negative (A-)" ,3:"B RhD positive (B+)", 4:"B RhD negative (B-)",
             5:"O RhD positive (O+)",6:"O RhD negative (0-)",7:"AB RhD positive (AB+)",8:"AB RhD negative (AB-)"}
b_list=list(b_types.values())
var_blood.set("selct blood type")
font1=('Times',12,'normal')
blood=Label(root, text="Blood Type :",width=20,bg="powder blue",font=("bold", 12)).place(x=60,y=450)
from tkinter import ttk
blood=ttk.Combobox(root,value=b_list,textvariable=var_blood,font=font1).place(x=200, y=450)


heart_check = IntVar()  
lungs_check = IntVar() 
liver_check =IntVar() 
kidney_check =IntVar() 

el_dnt50=Label(root,text="you can donate :",width=15,bg="powder blue",font=("bold",12)).place(x=60,y=500)  
heart=Checkbutton(root, text = "HEART",bg="powder blue",variable = heart_check,onvalue=1,font=10).place(x=200,y=500)
lungs= Checkbutton(root, text = "LUNGS",bg="powder blue",variable = lungs_check,onvalue=1,font=10).place(x=300,y=500)
liver=Checkbutton(root, text = "LIVER",bg="powder blue",variable = liver_check,onvalue=1,font=10).place(x=200,y=550)
kidney=Checkbutton(root, text = "KIDNEYS",bg="powder blue",variable = kidney_check,onvalue=1,font=10).place(x=300,y=550)


btn=Button(root, text="SUMBIT",command=save_donor,fg='blue').place(x=200, y=600)

def ad_logout():
    logout_frame2 = Frame(root, bd=12, relief=RIDGE, padx=20, bg="white")
    logout_frame2.place(x=510, y=100, width=980, height=680)
    a_logout.place_forget()


def admin_page():
   
         

         
    global userid,psd
    a_logout=Button(root, text="Logout",command=ad_logout,fg='blue',width=10,font=("bold",11))
    a_logout.place(x=1315, y=70)

    admin_frame1 = Frame(root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
    admin_frame1.place(x=510, y=100, width=980, height=300)

    admin_frame2 = Frame(root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
    admin_frame2.place(x=510, y=400, width=980, height=380)

    doc_title=Label(root,text="Register the Doctor ",width=20,bg="powder blue",font=("bold",15))
    doc_title.place(x=800,y=100)

    docname=StringVar()
    doc_name=Label(root,text="Doctor's Name :",width=15,bg="powder blue",font=("bold",12))
    doc_name.place(x=550,y=150)
    d_name_entry=Entry(root,textvariable=docname,font=10)
    d_name_entry.place(x=700,y=150)

    hospname=StringVar()
    hosp_name=Label(root,text="Hospital Name :",width=15,bg="powder blue",font=("bold",12))
    hosp_name.place(x=550,y=200)
    h_name_entry=Entry(root,textvariable=hospname,font=10)
    h_name_entry.place(x=700,y=200)


    docemail=StringVar()
    email= Label(root, text="Email-id :",width=20,bg="powder blue",font=("bold", 12))
    email.place(x=550,y=250)
    email_entry = Entry(root,textvariable=docemail,font=10)
    email_entry.place(x=700,y=250)

    docph=StringVar()
    phone= Label(root, text="Mobile No :",width=20,bg="powder blue",font=("bold", 12))
    phone.place(x=550,y=300)
    phone_entry = Entry(root,textvariable=docph,font=10)
    phone_entry.place(x=700,y=300)

    doclic=StringVar()
    docl= Label(root, text="Doc's License No :",width=20,bg="powder blue",font=("bold", 12))
    docl.place(x=950,y=150)
    docl_entry = Entry(root,textvariable=doclic,font=10)
    docl_entry.place(x=1200,y=150)

    userid=StringVar()
    uid=Label(root, text="Userid",width=20,bg="powder blue",font=("bold", 12))
    uid.place(x=950,y=200)
    entry_uid= Entry(root,textvariable=userid,font=10)
    entry_uid.place(x=1200,y=200)


    psd = StringVar()
    pwd= Label(root, text="Password",width=20,bg="powder blue",font=("bold", 12))
    pwd.place(x=950,y=250)
    entry_pwd = Entry(root,textvariable=psd, show='*',font=10)
    entry_pwd.place(x=1200,y=250)
    

    def save_data():
        if docname.get() !="" and hospname.get()!="" and doclic.get()!="" and docemail.get()!="" and docph.get()!="" and psd.get()!="" and userid.get()!="":
            print(docname.get(),hospname.get())
            mydb = mc.connect(host="localhost",user="root",password="shan",database="donate")
            mycursor = mydb.cursor()
            mycursor.execute("""INSERT INTO doc_reg (DoctorName,Hospital,License,Emailid,MobileNo,Password,Userid) VALUES (%s,%s,%s,%s,%s,%s,%s)""", 
                            (docname.get(),hospname.get(),doclic.get(),docemail.get(),docph.get(),psd.get(),userid.get()))
            mydb.commit()
            print("----------------------------")
        else:
            not_fill()
            
        

    reg_btn=Button(root,text="Register",command=save_data,font=("bold",12))
    reg_btn.place(x=920,y=350)


    

def show_data(table):
    print(table)
    global e
    my_connect = mc.connect(
        host="localhost",
        user="root", 
        passwd="shan",
        database="donate"
    )
    my_conn = my_connect.cursor()
    ####### end of connection ####
    
    admin_frame2 = Frame(root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
    admin_frame2.place(x=510, y=400, width=980, height=380)

    ldbtn=Button(root,text="Show Donors List",command=lambda:show_data("save_donor"),font=("bold",12))
    ldbtn.place(x=530,y=420)

    ldocbtn=Button(root,text="Show Doctors List",command=lambda:show_data("doc_reg"),font=("bold",12))
    ldocbtn.place(x=680,y=420)

    if table=="doc_reg":
        my_conn.execute("desc doc_reg")
    if table=="save_donor":
        my_conn.execute("desc save_donor")
    a=[]
    for det in my_conn:
        b=det[0]
        a.append(b)
    i=530
    for j in range (len(a)):
        e = Entry(root, width=10, fg='blue',font=("bold",12)) 
        e.place(x=i, y=470) 
        e.insert(END, a[j])  
        i=i+100


    if table=="doc_reg":
        my_conn.execute("SELECT * FROM {}".format (table))
    if table=="save_donor":
        my_conn.execute("SELECT * FROM {}".format (table))
        
    k=500
    for student in  my_conn: 
        i=530
        k=k+20

        for j in range(0,len(student)):
            e = Entry(root, width=10, fg='black',font=("bold",12)) 
            e.place(x=i, y=k) 
            e.insert(END, student[j])
            i=i+100

    
    
    ldbtn=Button(root,text="Show Donors List",command=lambda:show_data("save_donor"),font=("bold",12))
    ldbtn.place(x=530,y=420)

    ldocbtn=Button(root,text="Show Doctors List",command=lambda:show_data("doc_reg"),font=("bold",12))
    ldocbtn.place(x=680,y=420)


def doc_page():

    global a_logout,s_blood
    a_logout=Button(root, text="Logout",command=ad_logout,fg='blue',width=10,font=("bold",11))
    a_logout.place(x=1315, y=70)

    admin_frame1 = Frame(root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
    admin_frame1.place(x=510, y=100, width=980, height=300)

    
    doc_title=Label(root,text="Upadte Your Details",width=20,bg="powder blue",font=("bold",15))
    doc_title.place(x=800,y=100)

    email_d=StringVar()
    doc_name=Label(root,text=" Email:",width=15,bg="powder blue",font=("bold",12))
    doc_name.place(x=550,y=150)
    d_name_entry=Entry(root,textvariable=email_d,font=10)
    d_name_entry.place(x=700,y=150)

    phone_d=StringVar()
    hosp_name=Label(root,text="Hospital Name :",width=15,bg="powder blue",font=("bold",12))
    hosp_name.place(x=550,y=200)
    h_name_entry=Entry(root,textvariable=phone_d,font=10)
    h_name_entry.place(x=700,y=200)


    def update_doc():
        print(email_d.get())
        mydb = mc.connect(host="localhost",user="root",password="shan",database="donate")
        mycursor = mydb.cursor()
        if email_d.get()!="":
            mycursor.execute("update doc_reg set Emailid='{}' where Userid='{}'".format(email_d.get(),user.get()))
            mydb.commit()

        if phone_d.get()!="":
            mycursor.execute("update doc_reg set MobileNo='{}' where Userid='{}'".format(phone_d.get(),user.get()))
            mydb.commit()

    btn=Button(root, text="SUMBIT",command=update_doc,fg='blue').place(x=700, y=250)



    admin_frame2 = Frame(root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
    admin_frame2.place(x=510, y=400, width=980, height=380)



    ldbtn=Button(root,text="Show Donors List",command=lambda:doc_show("save_donor"),font=("bold",12))
    ldbtn.place(x=530,y=420)

    s_blood=StringVar()
    b_types={1:"A RhD positive (A+)",2:"A RhD negative (A-)" ,3:"B RhD positive (B+)", 4:"B RhD negative (B-)",
                5:"O RhD positive (O+)",6:"O RhD negative (0-)",7:"AB RhD positive (AB+)",8:"AB RhD negative (AB-)"}
    b_list=list(b_types.values())
    var_blood.set("select blood type")
    font1=('Times',12,'normal')
    blood=ttk.Combobox(root,value=b_list,textvariable=s_blood,font=font1).place(x=1000, y=420)

    ldbtn=Button(root,text="Search",command=lambda:doc_show("search_donor"),font=("bold",12))
    ldbtn.place(x=1230,y=420)



def doc_show(table):
    
    admin_frame2 = Frame(root, bd=12, relief=FLAT, padx=20, bg="powder blue")
    admin_frame2.place(x=530, y=460, width=950, height=300)

    db=mc.connect(host='localhost', user='root', password='shan', database='donate')
    mycursor=db.cursor()
    mycursor.execute("desc save_donor")
    a=[]
    for det in mycursor:
        b=det[0]
        a.append(b)
    i=530
    for j in range (len(a)):
        e = Entry(root, width=10, fg='blue',font=("bold",12)) 
        e.place(x=i, y=470) 
        e.insert(END, a[j])  
        i=i+100
    if table=="search_donor" :
        print("============")
        qu="select * from save_donor where B_type='{}'".format(s_blood.get())
        print(qu)
        mycursor.execute(qu)
        print(mycursor)
    if table=="save_donor" :
        mycursor.execute("select * from save_donor ")

    k=500
    for student in  mycursor: 
        i=530
        k=k+20

        for j in range(0,len(student)):
            e = Entry(root, width=10, fg='black',font=("bold",12)) 
            e.place(x=i, y=k) 
            e.insert(END, student[j])
            i=i+100

def login(table):
    db=mc.connect(host='localhost', user='root', password='shan', database='donate')
    mycursor=db.cursor()
    mycursor.execute("use donate")
    if table=="admin" :
        mycursor.execute('SELECT Admin_id FROM admin WHERE Admin_id = %s AND Password = %s', (user.get(),pswd.get()))
        db_user=str(mycursor.fetchone())
        mycursor.execute('SELECT Password FROM admin WHERE Admin_id = %s AND Password = %s', (user.get(), pswd.get()))
        db_psd=str(mycursor.fetchone())
        usr=user.get()
        pin=pswd.get()
    if table =="doc_reg" :
        mycursor.execute('SELECT Userid FROM doc_reg WHERE Userid = %s AND Password = %s', (user.get(),pswd.get()))
        db_user=str(mycursor.fetchone())
        
        mycursor.execute('SELECT Password FROM doc_reg WHERE Userid = %s AND Password = %s', (user.get(),pswd.get()))
        db_psd=str(mycursor.fetchone())
        
    db_user=db_user.replace('(',"")
    db_user=db_user.replace(',',"")
    db_user=db_user.replace("'","")
    db_user=db_user.replace(')',"")

    db_psd=db_psd.replace('(',"")
    db_psd=db_psd.replace(',',"")
    db_psd=db_psd.replace("'","")
    db_psd=db_psd.replace(')',"")

    if user.get()==db_user:
        if pswd.get()==db_psd:
            if table=="admin":
                admin_page()
            if table=="doc_reg":
                doc_page()
        else:
            err_psd=Label(root,text="Wrong Credentials",width=40,font=("bold", 10)).place(x=850,y=80)
    else:
        login_error()


a_login=Button(root, text="Admin Login",command=lambda:login("admin"),fg='blue',width=10,font=("bold",11)).place(x=1315, y=40)
# #doctors login
d_login=Button(root, text="Doctor's Login",command=lambda:login("doc_reg"),fg='blue',width=10,font=("bold",11)).place(x=580, y=40)

user=StringVar()
l_user=Label(root,text="User Id:",width=10,bg="white",font=("bold",12)).place(x=700,y=40)
entry_l_user=Entry(root,textvariable=user,font=("bold",12)).place(x=800,y=40)

pswd=StringVar()
l_user=Label(root,text="Password",width=10,bg="white",font=("bold",12)).place(x=950,y=40)
entry_l_user=Entry(root,textvariable=pswd,show='*',font=("bold",12)).place(x=1050,y=40)

root.mainloop()

