
def getProfile(id):
    #con = sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(id)
    cursor=con.execute(cmd)
    profile = None
    for row in cursor:
        profile=row;
    con.close()
    return profile

def FetchInfo(id):
    #con = sqlite3.connect("FaceBase1.db")
    cmd = "UPDATE People SET Visits=Visits+1 WHERE ID="+str(id)
    cur=con.execute(cmd)
    profile = getProfile(id);
    name = profile[1]
    gender = profile[2]
    city = profile[3]
    age = profile[4]
    visits = profile[5]
    purpose = profile[6]
    mobile = profile[7]                          # Change
    sm=0
    sm+=(visits/50 * 100)
    if(city == "Sangli"):
        sm+=(10);
    elif(city == "Miraj"):
        sm+=(30);        
    elif(city == "Pune"):
        sm+=(50);
    elif(city == "Mumbai"):
        sm+=(70);
   # elif(60 < age < 80 or purpose == "Urgent"):
       # excecFile('SMS.py')
        
    if(0 < age < 20):
        sm+=20
    elif(20 < age < 40):
        sm+=40
    elif(40 < age < 60):
        sm+=60
    
    if(purpose == "Meeting"):
        sm+=50
    elif(purpose == "Invitation"):
        sm+=30
    elif(purpose == "Personal"):
        sm+=10;
    print sum;

    if(sum > 150 or purpose == "Urgent" or 60<age<80 or ):
        SendSMS(name,gender,city,purpose,"9604091697");
    #else:
        #Code for Speaking....
