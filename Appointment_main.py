from tkinter import *

window=Tk()
window.title("Car Booking")
window.geometry("400x400")
window.config(bg="grey")
def sel():
    if(var1.get()=="" or var2.get()=="" or var3.get()=="" or var4.get()=="" or var5.get()==""  
or var6.get()==""):
        
        L.config(text="Fill all the fields",font=("Times New Roman",20),fg="red")
    elif(not(var4.get().isdigit()) or not(var4.get().isdigit()) ):
        L.config(text="Mobile and Form should be numbers",font=("Times New Roman",20),fg="red")
    else:
        s=var1.get()+var2.get()+var3.get()+var4.get()+var5.get()+var6.get()
        L.config(text=s,font=("Times New Roman",20),fg="Black")
var1,var2,var3,var4,var5,var6=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
l1=Label(window, text="CAR BOOKING",font=("Times New Roman",20),fg="black",bg="grey")
l1.grid(row=0,column=1)

l2=Label(window,text="Owner's Name", font=(
            'georgia 18 bold'),bg="grey")
l2.grid(row=1,column=0)

e2=Entry(window,width=50,bd=5,textvariable=var1)
e2.grid(row=1,column=1)

l3=Label(window,text="Age", font=(
            'georgia 18 bold'),bg="grey")
l3.grid(row=2,column=0)

e3=Entry(window,width=50,bd=5,textvariable=var2)
e3.grid(row=2,column=1)

l4=Label(window,text="Entry Time", font=(
            'georgia 18 bold'),bg="grey")
l4.grid(row=3,column=0)

e4=Entry(window,width=50,bd=5,textvariable=var3)
e4.grid(row=3,column=1)

l5=Label(window,text="Phone Number", font=(
            'georgia 18 bold'),bg="grey")
l5.grid(row=4,column=0)

e5=Entry(window,width=50,bd=5,textvariable=var4)
e5.grid(row=4,column=1)

l6=Label(window,text="Gender ", font=(
            'georgia 18 bold'),bg="grey")
l6.grid(row=5,column=0)

e6=Entry(window,width=50,bd=5,textvariable=var5)
e6.grid(row=5,column=1)

l7=Label(window,text="Location", font=(
            'georgia 18 bold'),bg="grey")
l7.grid(row=6,column=0)

e7=Entry(window,width=50,bd=5,textvariable=var6)
e7.grid(row=6,column=1)


L=Label(window,bg="grey")
L.grid(row=10,column=1)
b=Button(window, text="Add Booking", width=20,
                             height=2,command=sel,bg="green").grid(row=8,column=1)

window.mainloop()

