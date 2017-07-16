import sqlite3
import SMS
import PyMongo

def FetchInfo(id):
    profile1 = PyMongo.getProfile1(id);
    #print profile1
	
    profile2 = PyMongo.getProfile2(id);
    #print profile2
	
    name = profile1[0]
    gender = profile1[1]
    city = profile2[0]
    age = profile2[1]
    purpose = profile2[2]
    time=profile2[3];
    sm=0
    
    if(city == "Sangli"):
        sm+=(10);
    elif(city == "Miraj"):
        sm+=(30);        
    elif(city == "Pune"):
        sm+=(50);
    elif(city == "Mumbai"):
        sm+=(70);
    #elif(60 < age < 80 or purpose == "Urgent"):
        #execfile('SMS.py')
        
    if(0 < age < 20):
        sm+=20
    elif(20 <= age < 40):
        sm+=40
    elif(40 <= age < 60):
        sm+=60
    
    if(purpose == "Meeting"):
        sm+=50
    elif(purpose == "Invitation"):
        sm+=30
    elif(purpose == "Personal"):
        sm+=10;
        
    print sm;
    print purpose
    print city
    print age

    if(sm > 150 or 60 < age < 80 or purpose=="Urgent"):
        SMS.SendSMS(name,gender,city,purpose,mobile="9604091697")
        
        
    else:
        new_profile1=PyMongo.getProfile1(id)
        new_profile2=PyMongo.getProfile2(id)
        PyMongo.SCInsert(id,sm,time)
        PyMongo.SCSchedule()
        #SMS.SendSMS(new_profile1[1],new_profile1[2],new_profile2[1],new_profile2[3],new_profile1[3]);
        
		
    #else:
        #Code for Speaking....
