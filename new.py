import sys
sys.path.append('C://Users//Swapnil//website//music//script//')
import Main_Runner
import Predictor
import Trainer
from db_fetch import *

def ab():
	
	a,b=test_get(1000,20000)
	print(a)
	a,b=test_data(a,b)
	clf = joblib.load('MLP.pkl')
	trained_target=clf.predict(a)
	ans=trained_target

	return ans