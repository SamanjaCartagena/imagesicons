# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 15:06:04 2023

@author: c.samanja09
"""
from tkinter import *
from PIL import ImageTk,Image

root= Tk()
root.title('Learn how to code at Codemy.com')
#root.iconbitmap('logo.ico')


my_img=ImageTk.PhotoImage(Image.open("logo.png"))

my_label= Label(image=my_img)
my_label.pack()


button_quit= Button(root,text="Exit Program", command=root.quit)
button_quit.pack()
root.mainloop()
