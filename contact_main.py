#!/usr/bin/env python
# coding: utf-8

# In[1]:
def Ok0():
    import os
    os.system('after_login.py')

import mysql.connector


# In[2]:


mydb=mysql.connector.connect(host="localhost",user="root",password="root@123", database="INT213project")


# In[5]:


from tkinter import *
root = Tk() 

def register():
    v1 = var1.get()
    v2 = var2.get()
    v3 = var3.get()
    v4 = var4.get()
    v5 = var5.get()
    
    if v1 == "":
        error()
    elif v2 == "":
        error()
    elif v3 == "":
        error()
    elif v4 == "":
        error()
    elif (v5 == "" ):
        error()
    else:
        success()

def delete():
    root1.destroy()

def delete1():
    root2.destroy()

def error():
    global root1
    root1 = Toplevel(root)
    root1.geometry("150x90")
    root1.title("Warning!")
    Label(root1, text = "All fields required", fg = "red").pack()
    Button(root1, text = "OK", command = delete).pack()

def success():
    global root2
    root2 = Toplevel(root)
    root2.geometry("150x90")
    root2.title("Warning!")
    Label(root2, text = "Registration Sucess!", fg = "green").pack()
    Button(root2, text = "OK", command = delete1).pack()
    mydb=mysql.connector.connect(host="localhost",user="root",password="root@123",database="INT213project")
    mycs=mydb.cursor()
    sql="INSERT INTO python1(fullname,email, gender, country,phone) VALUES(%s,%s,%s,%s,%s)"
    val=(var1.get(),var2.get(),var3.get(),var4.get(),var5.get())
    mycs.execute(sql,val)
    mydb.commit()
    print(mycs.rowcount,"inserted sucessfully")

root.geometry("500x500")
root.config(bg="light blue")

root.title('contact form')


label_0 =Label(root,text="Contact Us", width=20,font=("bold",20), bg="orange")

label_0.place(x=90,y=60)


label_1 =Label(root,text="FullName", width=20,font=("bold",10))
label_1.place(x=68,y=130)

var1=StringVar()
entry_1=Entry(root,textvariable=var1)
entry_1.place(x=240,y=130)

label_3 =Label(root,text="Email", width=20,font=("bold",10))
label_3.place(x=68,y=180)
var2=StringVar()
entry_3=Entry(root,textvariable=var2)
entry_3.place(x=240,y=180)


label_4 =Label(root,text="Gender", width=20,font=("bold",10))
label_4.place(x=70,y=230)


var3=IntVar()

Radiobutton(root,text="Male",padx= 1, variable= var3, value=1).place(x=250,y=230)
Radiobutton(root,text="Female",padx= 20, variable= var3, value=2).place(x=300,y=230)


label_5=Label(root,text="Country",width=20,font=("bold",10))
label_5.place(x=70,y=280)

country=[ 'India' ,'US' , 'UK']

var4=StringVar()
droplist=OptionMenu(root,var4, *country)
droplist.config(width=15)
var4.set('Country')
droplist.place(x=240,y=280)

label_6 =Label(root,text="Phone number", width=20,font=("bold",10))
label_6.place(x=70,y=330)

var5=StringVar()
entry_6=Entry(root,textvariable=var5)

entry_6.place(x=250,y=330)



b=Button(root, text='Submit' ,command=register, width=20,bg="black",fg='white')

b1=Button(root, text='back' ,command=Ok0, width=20,bg="black",fg='white')
b1.place(x=350,y=380)

b.place(x=180,y=380)


root.mainloop()


# In[4]:


import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root@123",database="INT213project")
mycs=mydb.cursor()
mycs.execute("SELECT * from python1")

myresult=mycs.fetchall()
for i in myresult:
    print(i)


# In[ ]:




