from db_fetch import *;
from pymongo import MongoClient
import pymongo
import numpy as np
import json
client = MongoClient('localhost', 27017)
db = client.project
a,b=test_get(0,500000)

print(type(a))

ls=[]
db.test4_data.delete_many({})
ink=0
for x in a:
    if b[ink] in [0,2]:
        x['type']=b[ink]
        ink+=1
        ls.append(x)

print(ls)
        
db.test4_data.insert_many(ls)

    

    