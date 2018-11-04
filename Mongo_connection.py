from io import open
from pymongo import MongoClient
import pymongo
import numpy as np
from .Category import *


class Database_Manager:
    client =MongoClient('localhost', 27017)
    db=client.project
    
    def MLPModel_fetch_Train_data(self):
        train_list=self.db.train_data.find()
        
        
        cursor =train_list.sort('train.type',pymongo.ASCENDING)
        dataset =[]
        dataTarget=[]
        for document in cursor:
            data_dict={}
            for feature in attr_list:
                if feature=='protocol_type' or feature=='service' or feature== 'flag':
                    data_dict[feature] = document['train'][feature]
                elif feature is not 'type':
                    try:
                        data_dict[feature] = document['train'][feature].encode('ascii')
                    except:
                        data_dict[feature] = document['train'][feature]
            dataset.append(data_dict)
            dataTarget.append(int(document['train']['type']))
        
        return np.array(dataset),np.array(dataTarget)
    
    def MLPModel_fetch_Test_data(self):
        
        test_list=self.db.test_data.find()
        cursor = test_list
        testset =[]
        dataTarget =[]
        
        for document in cursor :
            data_dict={}
            for feature in attr_list:
                if feature=='protocol_type' or feature=='service' or feature == 'flag':
                    data_dict[feature] = document['test'][feature]
                if feature is not 'type':
                    try:
                        data_dict[feature] = document['test'][feature].encode('ascii')
                    except:
                        data_dict[feature] = document['test'][feature]
            testset.append(data_dict)
            dataTarget.append(int(document['test']['type']))
            
        return np.array(testset),np.array(dataTarget) 
    
    
    
    
#db=Database_Manager()
#a,b=db.MLPModel_fetch_Train_data()
#c,d=db.MLPModel_fetch_Test_data()

    
        