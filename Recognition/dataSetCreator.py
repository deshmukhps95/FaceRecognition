import cv2,sys
import os
import numpy as np
import sqlite3
import pyttsx
import urllib
import PyMongo


#url = "http://192.168.43.1:8080/shot.jpg";

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

cam = cv2.VideoCapture(0);

engine = pyttsx.init('sapi5');
engine.say("Please look towards camera")
#engine.say("Namaskaar !")
#cv2.waitKey(2);
#engine.say("Welcome to collector office ,Saanglee! ");
#engine.runAndWait()

        
sampleNum=0;

while(True):
    ret,img=cam.read();
    
    #imgResponse = urllib.urlopen(url);
    #imgNp=np.array(bytearray(imgResponse.read()),dtype=np.uint8)
    #img=cv2.imdecode(imgNp,-1)
    
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces=faceDetect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    
    
    for(x,y,w,h) in faces:
        
        sampleNum=sampleNum+1
        cv2.imwrite('dataSet/User.'+str(int(PyMongo.GetID(Name)))+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        
    cv2.imshow("Please look here( src: webcam1)",img);
    
    cv2.waitKey(100)
    
    if(sampleNum >= 20):
        break
    
#imgResponse.release()
#sys.exit()
#cam.release()
engine.say("Thank you")
cv2.destroyAllWindows()
execfile("trainer.py")
