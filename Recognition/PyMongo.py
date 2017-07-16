from pymongo import MongoClient
from datetime import datetime
from time import gmtime, strftime
import SMS
global SMS

client = MongoClient('localhost:27017')
db = client.my_dbase

# Function to insert data into mongo db
def insertNew(Name,Gender,City,Age,Purpose,Mobile):
    id=getNextSequence(db.counters,"uid")
    try:
        db.userInfo.insert_one(
            {
            "id":id,
            "name":Name,
            "gender":Gender,
            "mobile":Mobile,
            })
        db.visitRecord.insert_one({
            "id":id,
            "city":City,
            "age":Age,
            "purpose":Purpose,
            "date":datetime.now().strftime ("%Y%m%d"),
            "time":strftime("%H:%M:%S",gmtime())
            })

        print '\nInserted data successfully\n'
    
    except Exception, e:
        print str(e)



def insertPrev(Id,City,Age,Purpose):
    try:
        db.visitRecord.insert_one({
            "id":Id,
            "city":City,
            "age":Age,
            "purpose":Purpose,
            "date":datetime.now().strftime ("%Y%m%d"),
            "time":strftime("%H:%M:%S",gmtime())
            })
        
        print '\nInserted data successfully\n'
    
    except Exception, e:
        print str(e)

        

# function to read records from mongo db
def read():
    try:
        Col = db.userInfo.find()
        print '\n All data from EmployeeData Database \n'
        for user in Col:
            print user

    except Exception, e:
        print str(e)
        

# Function to update record to mongo db
def update():
    try:
        criteria = raw_input('Enter Name :')
        gender = raw_input('Enter Gender :')
        city = raw_input('Enter city :')
        age = raw_input('Enter age :')
        purpose = raw_input('Enter Purpose :')

        db.visitRecord.update_one(
            {"name": criteria},
            {
            "$set": {
                "city":city,
                "age":age,
                "purpose":purpose
            }
            }
        )
        print "\nRecords updated successfully\n"    
    
    except Exception, e:
        print str(e)

# Function to delete record from mongo db
def delete():
    try:
        criteria = raw_input('\nEnter employee id to delete\n')
        db.userInfo.delete_many({"id":criteria})
        print '\nDeletion successful\n' 
    except Exception, e:
        print str(e)

def getNextSequence(collection,name):  
    return collection.find_and_modify(query= { 'id': name },update= { '$inc': {'seq': 1}}, new=True ).get('seq')


def GetID(name):
    try:
        for obj in db.userInfo.find():
            if(obj['name'] == name):
                return obj['id']
                break;
    except Exception, e:
        print str(e)
		
def GetName(id):
    try:
         for obj in db.userInfo.find():
            if(obj['id'] == id):
                return obj['name']
                break;
    except Exception, e:
        print str(e)
		
def getProfile1(id):
    ls=[]
    try:
        for obj in db.userInfo.find():
            if(obj['id'] == id):
                ls.append(str(obj['name']))
                ls.append(str(obj['gender']))
                ls.append(str(obj['mobile']))
                return ls
                break;
    except Exception, e:
        print str(e)
		
def getProfile2(id):
    try:
        ls=[]
        for obj in db.visitRecord.find():
            if(obj['id'] == id):
                ls.append(str(obj['city']))
                ls.append(str(obj['age']))
                ls.append(str(obj['purpose']))
                ls.append(str(obj['time']))
                return ls
                break;
    except Exception, e:
        print str(e)
        
def SCInsert(id,prio,atime):
    db.sc.insert_one({
        "uid":id,
        "p":prio,
        "at":atime
        });
def SCSchedule():
    l=[]

    for obj in db.sc.find():
        l.append(obj)

    
    #print(l)
    m=[]
    m=sorted(l[2:],key=lambda x:x['p'],reverse=True)
    #l.sort(key=attrgetter('p'),reverse=True)
    #print "hello m"
    #print m


    n=[]    
    n.append(l[0])
    if len(l) >=2:
        n.append(l[1])
    for i in m:
        n.append(i)
    #print "hello n"
    #print(n)
    #db.sc.remove({},{justOne:True},reverse=True)

    #db.sc.remove({},{justOne:True})

    db.sc.remove()
    token=1;
    for obj in n:
        #print(obj[1])
        #db.sc.insert_one(dict(obj[0]),dict(obj[1]),dict(obj[3]),dict(obj[4]))
        str1=obj['uid']
        #str2=str(obj['i'])
        str3=str(obj['p'])
        str4=str(obj['at'])
        db.sc.insert_one({'uid':float(str1),'p':float(str3),'at':str4})
        profile=getProfile1(int(str1))
        #print(profile + str1 )
        mobile=profile[2]
        SMS.SendSMS(profile[0],profile[1],'',token,mobile)
        token+=1;
