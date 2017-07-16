from Tkinter import *
import datetime
import Tkinter as Tk
import tkMessageBox
import tkFont
from PIL import Image

root = Tk.Tk()

def new():
	execfile("E:/face2/Recognition/5.py")
	#sp.Popen(['python','5.py'])
	#sp.Popen.terminate(p1)
	
	
def prev():
	execfile("E:/face2/Recognition/6.py")

#root.minsize(width=666,height=666)
#root.maxsize(width=666,height=666)
width=600
height=400
background_image=Tk.PhotoImage(file="E:/face2/Gui/marbles.gif")
background_label = Tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.wm_geometry("600x1000+20+40")
label_head=Label(root,text="Virtual Assistant",font=("Lucida Fax",23),fg="cyan",bg="black");

f = tkFont.Font(label_head, label_head.cget("font"))
f.configure(underline = True)   

label_head.configure(font=f)
label_head.pack()
label_b1=Label(root,text="")
label_b1.pack()
label_1= Label(root,text="Welcome to Collector Office Virtual assistant",font=("Helvetica",20),fg="red",bg="black")
label_1.pack()
label11= Label(root,text="General Information About This project",font=("Helvetica",15),fg="blue",bg="black")
label11.pack()
label_2= Label(root,text="I am a Smart Virtual assistant will help you schedule your meeting",fg="white",bg="black")
label3= Label(root,text="with Mr. COllector. Please interact with the me to be in my memory",fg="white",bg="black")
label4= Label(root,text="so that I can remember you.If you are new to interact with me",fg="white",bg="black")
label5= Label(root,text="please select new user and tell me required details which will be  ",fg="white",bg="black")
label6= Label(root,text="helpful for me to know you.If you have previously visited please select 'previously",fg="white",bg="black")
label7= Label(root,text=" visited' please select appropriate option, so that i can identify you and notify every one if necessary.",fg="white",bg="black")
label8= Label(root,text="Thank you.",fg="white",bg="black")
label13= Label(root,text="")
label14= Label(root,text="")
label15= Label(root,text="")
label16= Label(root,text="")
label17= Label(root,text="Developed By:",fg="white", bg="black")
label18= Label(root,text="  Vaibhav B. Revanwar",fg="white",bg="black")
label19= Label(root,text="  Pritam V. Kulkarni",fg="white",bg="black")
label20= Label(root,text="  Prasad Manedeshmukh",fg="white",bg="black")



label_2.pack()
label3.pack()
label4.pack()
label5.pack()
label6.pack()
label7.pack()
label8.pack()

label13.pack()
label14.pack()
label17.pack()

label18.pack()
label19.pack()
label20.pack()

b1 = Button(root, text="New User? Please click here",command=new)
b2 = Button(root, text="Previously visited? Please click here",command=prev)

 
b1.pack()
b2.pack()


screen_w =root.winfo_screenwidth()
screen_h =root.winfo_screenheight()

x = (screen_w/2)-(width/2)
y = (screen_h/2)-(height/2)
root.geometry('%dx%d+%d+%d' %(600,450,x,y))
#load=Tk.PhotoImage(file="/home/pi/Desktop/new_project/Logo_384_1.png")
#img10=Label(root,image=load)
#img10.image=load
#img10.place(x=0,y=0)
root.mainloop()
