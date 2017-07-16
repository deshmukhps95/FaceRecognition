import cv2,os
import numpy as np
import pickle
import sqlite3
import pyttsx

import urllib2
import cookielib
from getpass import getpass
import sys
from stat import *

def SendSMS(name,gender,city,purpose,mobile):
    initial=""
    if(gender == 'Male'):
        initial = "Mr."
    else:
        initial = "Mrs."

      
    if(mobile == "9604091697") :    
        message = initial+" "+name+" from" +city+" is waiting ! (" + purpose + ")"
    else:
        token=purpose
        message = initial+ " "+ name+ "HAVE BEEN APPOINTED  for token : " + str(token) +"!!" ;
        
        
    number = mobile
    
    username = "9604091697"
    passwd = "oklahomauniversity"


    message = "+".join(message.split(' '))

    #logging into the sms site
    url ='http://site24.way2sms.com/Login1.action?'
	
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

    #For cookies

    cj= cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	#Adding header details
    opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
    
    try:
        usock =opener.open(url, data)
    except IOError:
        print "error"
        #return()


    jession_id =str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
	
    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
        print "error"
        #return()
    print "message sent" 
    #return ()
    
    engine = pyttsx.init('sapi5');
    cv2.waitKey(2);
    engine.say("You have been successfully scheduled")
    #execfile("3.py")
    #engine.say("Namaskaar !")
    #cv2.waitKey(2);
    #engine.say("Welcome to collector office ,Saanglee! ");
    engine.runAndWait()
#SendSMS('Pritam','M','mumbai','urgent','9604091697')
    
