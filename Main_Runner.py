#from Mongo_Con import DB_manager 
from Trainer import Trainer
from Predictor import Predictor
from db_fetch import *
import  pandas as pd
import time


class MLP_Runner:
    trainer = Trainer()
    predictor = Predictor()
    

    def data_load(self):
        dataset, datatarget, T_len = self.db.MLP_fetch_data()
        return dataset, datatarget, T_len

    def train(self, dataset, datatarget, T_len):
        print("check......................................! \n")
        data_set, data_target, test_set, test_target = self.trainer.one_hot_encode_normalize(dataset, datatarget, T_len)
        print("done.............")
        
        self.trainer.Train(data_set, data_target)
        
        #print(test_set[:1000])
        #self.predictor.predict(test_set, test_target)
        a,b=test_get(1000,22000)
        a,b=self.trainer.test_data(a,b)
        return self.predictor.predict(a,b)
        
        
        


#dataset, datatarget, T_len = DB_manager().MLP_fetch_data()
#dataset,datatarget,T_len=fetch()
#dataset=pd.DataFrame(dataset)
#print(dataset)
#runner.train(dataset, datatarget, T_len)


