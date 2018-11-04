from sklearn.externals import joblib
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import confusion_matrix
from .db_fetch import *
from .Trainer import *
import os

class Predictor:
    def predict(self, test_set, test_target):
        clf = joblib.load(os.path.join(os.getcwd(), 'music', 'MLP.pkl'))
        trained_target = clf.predict(test_set)
       	return trained_target
        #print(trained_target)
        #print(test_target)
        #print(confusion_matrix(test_target, trained_target, labels=[0,2]))
        #print(classification_report(test_target, trained_target))
        
        
        
        #print(precision_recall_fscore_support(test_target,trained_target))
        
"""
l=5000
b=9600
a,b=test_get(l,b)
t=Trainer()
a,b=t.test_data(a,b)

p=Predictor()


p.predict(a,b)"""
