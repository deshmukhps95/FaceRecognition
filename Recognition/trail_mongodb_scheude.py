import PyMongo
from pymongo import MongoClient
from datetime import datetime
from time import gmtime, strftime
from operator import attrgetter
client = MongoClient('localhost:27017')
db = client.my_dbase

l=[]

for obj in db.sc.find():
    l.append(obj)
    
print(l)
m=[]
m=sorted(l[2:],key=lambda x:x['p'],reverse=True)
#l.sort(key=attrgetter('p'),reverse=True)
print "hello m"
print m


n=[]
n.append(l[0])
n.append(l[1])
for i in m:
    n.append(i)
print "hello n"
print(n)
#db.sc.remove({},{justOne:True},reverse=True)

#db.sc.remove({},{justOne:True})

db.sc.remove()

for obj in n:
    #print(obj[1])
    #db.sc.insert_one(dict(obj[0]),dict(obj[1]),dict(obj[3]),dict(obj[4]))
    str1=str(obj['uid'])
    str2=str(obj['i'])
    str3=str(obj['p'])
    str4=str(obj['at'])#arrival time
    db.sc.insert_one({'uid':float(str1),'i':float(str2),'p':float(str3),'at':float(str4)})
                      