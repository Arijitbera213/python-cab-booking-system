from tkinter import *
from tkinter import messagebox


def Ok():
    uname = e1.get()
    password = e2.get()

    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")


    elif(uname == "Admin" and password == "123"):

        messagebox.showinfo("","Login Success")
        import os
        os.system('after_login.py')
        root.destroy()

    else :
        messagebox.showinfo("","Incorrent Username and Password")


root = Tk()
root.title("UserLogin")
root.geometry("300x200")


global e1
global e2

Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")


Button(root, text="Login",bg="red", command=Ok ,height = 3, width = 13).place(x=10, y=100)

root.mainloop()
