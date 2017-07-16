import cv2,os
import numpy as np
import pickle
import sqlite3
import pyttsx
import urllib
import cookielib
from getpass import getpass
import sys
from stat import *
import PyMongo
import FetchInformation
global id


faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv2.VideoCapture(0);

# url for remote access
#url = "http://10.7.2.128:8080/shot.jpg";

rec=cv2.createLBPHFaceRecognizer();
rec.load("Recognizer\\trainingData.yml")
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1,1)

ls=[]
cnt=0

while(True):

    ret,img=cam.read();

    #code for remote access.....
    #imgResp = urllib.urlopen(url);
    #imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    #img=cv2.imdecode(imgNp,-1)
    
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    
    for(x,y,w,h) in faces:        
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf = rec.predict(gray[y:y+h,x:x+w])
        ls.append(id)
                    
    cnt+=1
    if(cnt==20):
        cnt=0
        id=max(ls)
        ls=[]
        profile = PyMongo.GetName(float(id));
        print profile
		
        engine = pyttsx.init('sapi5');
        engine.say("Namaskaar !")
        cv2.waitKey(2);
        engine.say("Welcome to collector office ,Saanglee!"+str(profile));
        cv2.waitKey(2)
        engine.say("Please fill the following information")
        cv2.waitKey(2)
        engine.runAndWait()
        city=raw_input("Enter city:")
        age=raw_input("Enter age:")
        purpose=raw_input("Enter purpose:")

        PyMongo.insertPrev(id,city,age,purpose)

        cv2.waitKey(3)

        engine.say("Thank you for the response !")
        engine.runAndWait()
        break
        cv2.imshow("Face",img);
      
    if(cv2.waitKey(1)==ord('q')):
        break;
		
cam.release()
cv2.destroyAllWindows() 
FetchInformation.FetchInfo(id)
#con.close()
