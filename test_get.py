
from io import open
from pymongo import MongoClient
import pymongo
import numpy as np
from Category import *

def test_get(leng,end):
    client = MongoClient('localhost', 27017)
    db = client.project
    dataset=[]
    dataTarget=[]
    
    test_cursor = db.test_data.find()
    cnt=0
    pi=0
    re=0
    for document in test_cursor:
        pi+=1
        if pi<leng:
            continue
        if pi >end:
            break
        
        tmp_dic = {}
        if int(document['test']['type']) in ls:
            
            re+=1
            for attr in attr_list:
               
                
                if attr=='protocol_type' or attr=='flag' or attr=='service':
                    tmp_dic[attr] = document['test'][attr]
                elif attr is not 'type':
                    
                    try:
                        tmp_dic[attr] = document['test'][attr].encode('ascii')
                    except:
                        tmp_dic[attr] = document['test'][attr]
                
            
            #print(int(document['test']['type']))    
            dataset.append(tmp_dic)
            dataTarget.append(int(document['test']['type']))
    
    
    
        
      
    
    return np.array(dataset),np.array(dataTarget)