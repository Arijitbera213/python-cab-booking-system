from tkinter import *          # import * means from which package we are importing
def ADD():
    x,y=s.get(),s1.get()
    if(not x or not y):
        L3.config(text="Please Enter all the fields",height=3,width=20, bg="purple",fg="white")
top=Tk()               #for creating window
top.geometry("1600x800")
top.config(bg="green")
s=StringVar()          #to fetch the value
s1=StringVar()
L1=Label(top,text="PICKUP POINT")   #L1 is object
L1.place(x=10,y=10)       # x ,y are coordinates
E1=Entry(top,bd=5, textvariable=s)   # s is the variable in which i am storing the value of the textbox
E1.place(x=100,y=10)
L2=Label(top,text="DESTINATION")  #L2 is object
L2.place(x=10,y=50)
E2=Entry(top,bd=5, textvariable=s1)
E2.place(x=100,y=50)
b1=Button(top,text="ADD", command=ADD,height=3,width=10,bg="blue",fg="white",activebackground="yellow",activeforeground='white')
b1.place(x=80,y=100)
L3=Label(top)
L3.place(x=80,y=150)
top.mainloop()