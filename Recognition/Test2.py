import cv2,sys
import os
import numpy as np
import sqlite3
import pyttsx
import urllib
import PyMongo
from Tkinter import *

import tkMessageBox
import tkFont
import G5
#------------------------------------------------------------------------

#GUI part

main = Tk() # creates root window
# all components of thw window will come here

main.title(" Naagarik Seva ")
root = Frame(main)

width=600
height=400

#background_image=Tk.PhotoImage(file="C:\Python27\imgres.jpg")
#background_label = Tk.Label(root, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_head=Label(root,text="Collector Office,Sangli.",font=("Lucida Fax",23),fg="cyan",bg="black");

f = tkFont.Font(label_head, label_head.cget("font"))

f.configure(underline = True)
label_head.grid(row=1,column=2)
#label_head.configure(font=f)
#label_head.pack()

l= Label(root,text="                                                         ")
l1 = Label(root,text="Name: ")
l2 = Label(root,text="Purpose: ")
l3 = Label(root,text="Age: ")
l4 = Label(root,text="Gender: ")
l5 = Label(root,text="City: ")

d1= Label(root,text=" ----------------------------------------------------------")
d2= Label(root,text=" ----------------------------------------------------------")
d3= Label(root,text=" ----------------------------------------------------------")
d4= Label(root,text=" ----------------------------------------------------------")
d5= Label(root,text=" ----------------------------------------------------------")

screen_w =root.winfo_screenwidth()
screen_h =root.winfo_screenheight()

x = (screen_w/2)-(width/2)
y = (screen_h/2)-(height/2)
main.geometry('%dx%d+%d+%d' %(800,250,x,y))



#dropdown for gender








    
def page():
    name=t1.get()
    age=t3.get()
    if( float(age).is_integer()):
        page =Tk()
        
        lp1 = Label(page,text="Data Entered Successfully")
        lp1.pack()
 # To keep GUI window running
def MainPage():
    gender=StringVar(main)
    choices={'Male','Female','Other'}
    gender.set('Male')
    popupmenu = OptionMenu(root,gender,*choices)


    #dropdown for city
    city=StringVar(main)
    choices1={'Sangli','Miraj','Pune','Mumbai'}
    city.set('Sangli')
    popupmenu1 = OptionMenu(root,city,*choices1)

    purpose=StringVar(main)
    choices2={'Personal','Meeting','Urgent','Invitation','Other'}
    purpose.set('Meeting')
    popupmenu2 =OptionMenu(root,purpose,*choices2)


    t1=Entry(root)
    t2=Entry(root)
    t3=Entry(root)
    t5=Entry(root)

    l.grid(row=2,column=1)
    l1.grid(row=4,column=1)
    t1.grid(row=4,column=3)
    d1.grid(row=4,column=2)

    l2.grid(row=5,column=1)
    popupmenu2.grid(row=5,column=3)
    d2.grid(row=5,column=2)

    l3.grid(row=6,column=1)
    t3.grid(row=6,column=3)
    d3.grid(row=6,column=2)

    l4.grid(row=7,column=1)
    ordopupmenu.grid(row=7,column=3)
    d4.grid(row=7,column=2)

    l5.grid(row=8,column=1)
    popupmenu1.grid(row=8,column=3)
    d5.grid(row=8,column=2)
    def gen_dropdown(*args):
        tgender=gender.get()

    def city_dropdown(*args):
        tcity=city.get()

    def purpose_dropdown(*args):
        tpurpose=purpose.get()

    gender.trace('w',gen_dropdown)
    city.trace('w',city_dropdown)
    purpose.trace('w',purpose_dropdown)
    def page1():
        Name = str(t1.get())
        Gender = str(gender.get())
        City = str(city.get())
        Age = str(t3.get())
        Purpose = str(purpose.get())
        #ls=[]
        #ls = G5.getGuiInfo()
        #print ls
        cam = cv2.VideoCapture(0);
        while(True):
            ret,img=cam.read();
            cv2.imshow("Face",img);
            cv2.waitKey(100) 
            if(sampleNum >= 20):
                break
    
        cv2.destroyAllWindows()
    b = Button(root,text="Continue",fg="red",bg="grey",command=page1)
    b.grid(row=9,column=2)
main.mainloop() # To keep GUI window running
