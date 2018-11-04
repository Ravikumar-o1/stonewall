from io import open
from pymongo import MongoClient
import pymongo
import numpy as np
from Category import *
#   from Mongo_Con import *

ls=[2]
def fetch():
    client = MongoClient('localhost', 27017)
    db = client.project
    dataset=[]
    dataTarget=[]
    training_cursor = db.train_data.find()
    #dataset.append(attr_list)
    cnt=0
    
    for document in training_cursor:
        tmp_dic = {}
        
        if int(document['train']['type']) in ls:
           
            
            cnt+=1
            for attr in attr_list:
               
                
                if attr=='protocol_type' or attr=='flag' or attr=='service':
                    tmp_dic[attr] = document['train'][attr]
                elif attr is not 'type':
                    
                    try:
                        tmp_dic[attr] = document['train'][attr].encode('ascii')
                    except:
                        tmp_dic[attr] = document['train'][attr]
                
                
                    
            dataset.append(tmp_dic)
            dataTarget.append(int(document['train']['type']))
    return np.array(dataset),np.array(dataTarget)


a,b=fetch()
print(len(a))
print(a)
print(b)