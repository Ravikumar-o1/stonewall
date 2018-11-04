from sklearn.externals import joblib
import random
from sklearn.feature_extraction import DictVectorizer
import collections
import numpy as np
from .Mongo_connection import Database_Manager
from sklearn.feature_selection import VarianceThreshold
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from .Category import *


class Trainer:
    
    def Train(self,train_set,train_target):
        clf=MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(25,10,6), learning_rate='adaptive',
                          random_state=1,max_iter=10000)
        print('.................working fine after clf object create...............................')
        clf.fit(train_set,train_target)
        joblib.dump(clf,'output/MLP.pkl')
        
        
    def one_hot_encode_normalize(self,dataset,datatarget,T_len):
        
       
        
        print("......................................fine working:............................................")
        vec = DictVectorizer()
        dataset = vec.fit_transform(dataset).toarray()
       
        
        print(dataset.shape)

       

        pca = PCA(n_components=20)
        pca.fit(dataset)

        data_set = pca.transform(dataset)
        

        print(data_set.shape)

        scaler = StandardScaler()
        scaler.fit(data_set)

        print(pca.explained_variance_ratio_)

        data_set = scaler.transform(data_set)
        test_data=data_set[T_len:]
        test_target=datatarget[T_len:]
        

        #print(collections.Counter(test_target))

        return data_set[:T_len], datatarget[:T_len],test_data,test_target
    
    
    def test_data(self,dataset,datatarget):
        print("......................................fine working:............................................")
        vec = DictVectorizer()
        dataset = vec.fit_transform(dataset).toarray()
         
        print(dataset.shape)
         
        
         
        pca = PCA(n_components=20)
        pca.fit(dataset)
         
        data_set = pca.transform(dataset)
         
         
        print(data_set.shape)
         
        scaler = StandardScaler()
        scaler.fit(data_set)
         
        print(pca.explained_variance_ratio_)
         
        data_set = scaler.transform(data_set)
         
         
         
        #print(collections.Counter(data_set))
         
        return data_set ,datatarget
    

def test_data(dataset,datatarget):
        print("......................................fine working:............................................")
        vec = DictVectorizer()
        dataset = vec.fit_transform(dataset).toarray()
         
        #print(dataset.shape)
         
        
         
        pca = PCA(n_components=20)
        pca.fit(dataset)
         
        data_set = pca.transform(dataset)
         
         
        #print(data_set.shape)
         
        scaler = StandardScaler()
        scaler.fit(data_set)
         
        #print(pca.explained_variance_ratio_)
         
        data_set = scaler.transform(data_set)
         
         
         
        #print(collections.Counter(data_set))
         
        return data_set ,datatarget
    