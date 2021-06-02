#!/usr/bin/env python
# coding: utf-8

# In[5]:


from tkinter import *

def Ok():
    import os
    os.system('login_connect.py')

root = Tk()


root.geometry("500x500")
root.config(bg="light blue")

root.title('Cab BOOKING')


b1=Button(root, text='Signin' , command=Ok,width=20,bg="black",fg='white')

b1.place(x=180,y=190)

root.mainloop()


# In[ ]:




