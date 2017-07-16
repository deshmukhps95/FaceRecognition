from Tkinter import *
import sqlite3
import pyttsx
import os,cv2
from PIL import Image
import numpy as np

def newuser():
    print "In New User"
 #   login = Tk()
    execfile("E:\\Face2\\Recognition\\dataSetCreator.py")
    execfile("E:\\Face2\\Recognition\\trainer.py")
    execfile("E:\\Face2\\Recognition\\detector.py")
   # f= Frame(login)
#    x=Label(f,text="You are New User")
 #   f.pack()
  #  x.pack()
    root.destroy()
    
def login():
    execfile("E:\\Face1\\Recognition\\detector.py")

	
def main():
 global root
 root = Tk()
 # Create the root (base) window where all widgets go
 l1 = Label(root, text="Hello Welcome")
 
 l1.grid(row=0)
 b1 = Button(root, text="New User",command=newuser)
 b2 = Button(root, text="Previously visited",command=login)
 
 b1.grid(row=2,column=1)
 b2.grid(row=2,column=2)

 root.mainloop()
main()
