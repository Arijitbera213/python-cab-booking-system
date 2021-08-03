#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *

def Ok0():
    import os
    os.system('book.py')
def Ok1():
    import os
    os.system('Appointment_main.py')
def Ok2():
    import os
    os.system('contact_main.py')
def Ok3():
    import os
    os.system('feddback.py')
    

root = Tk()


root.geometry("500x500")
root.config(bg="light blue")

root.title('Cab BOOKING')



b2=Button(root, text='book' ,command=Ok0, width=20,bg="black",fg='white')
b3=Button(root, text='appointment' ,command=Ok1, width=20,bg="black",fg='white')
b4=Button(root, text='contact' , command=Ok2,width=20,bg="black",fg='white')
b5=Button(root, text='feedback', command=Ok3,width=20,bg="black",fg='white')



b2.place(x=180,y=220)
b3.place(x=180,y=260)
b4.place(x=180,y=300)
b5.place(x=180,y=340)


root.mainloop()


# In[ ]:




