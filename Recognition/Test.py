from pymongo import MongoClient
from datetime import datetime
from time import gmtime, strftime
client = MongoClient('10.7.2.95:27017')
db = client.my_dbase
# Function to insert data into mongo db
def insertNew(Name,Gender,City,Age,Purpose):
    id=getNextSequence(db.counters,"uid")
    try:
        db.userInfo.insert_one(
            {
            "id":id,
            "name":Name,
            "gender":Gender,
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
def readUserInfo():
    try:
        Col = db.userInfo.find()
        print '\n All data from EmployeeData Database \n'
        for user in Col:
            print user

    except Exception, e:
        print str(e)
def readVisitInfo():
    try:
        Col = db.visitRecord.find()
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
    try:
        for obj in db.visitRecord.find():
            if(obj['id'] == id):
                return obj
                break;
    except Exception, e:
        print str(e)
def getProfile2(id):
    try:
        for obj in db.visitRecord.find():
            if(obj['id'] == id):
                return obj
                break;
    except Exception, e:
        print str(e)
def MainProgram():

    while(True):
    # chossing option to do CRUD operations
        selection = raw_input('\nSelect 1 to insert into user info,\n 2 insert into visit records , \n3 to read user info, \n4 to read visit records \n5Delete from UserInfo\n\n')
        
    
        if selection == '1':
            Name = raw_input('Enter Name :')
            Gender = raw_input('Enter Gender :')
            City = raw_input('Enter city :')
            Age = raw_input('Enter age :')
            Purpose = raw_input('Enter Purpose :')

            insertNew(Name,Gender,City,Age,Purpose)
        elif selection == '2':
            Id = raw_input("Enter ID:")
            City = raw_input('Enter city :')
            Age = raw_input('Enter age :')
            Purpose = raw_input('Enter Purpose :')

            insertPrev(Id,City,Age,Purpose)
            
        elif selection == '3':
            readUserInfo()
            
        elif selection == '4':
            readVisitRecords()
            
        elif selection == '5':
            
MainProgram()
