from Category  import *
from pymongo import MongoClient
# -------------import data from  file and posting it to database for easy of retrival ------------------
class Database_Insert:
    client = MongoClient('localhost', 27017)
    db = client.project
    def isfloat(self,value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    def trainInsert(self,file):
        self.db.train3_data.delete_many({})
        self.db.train3_data.create_index("train.type")
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                columns = line.split(',') 
                dic = {}
                for attr in attr_list:
                    element = columns[attr_list.index(attr)]
                    if element.isdigit():
                        element = int(element)
                    elif self.isfloat(element):
                        element = float(element)
                    dic[attr] = element
                print(dic)
                self.db.train3_data.insert_one({"train": dic})

    
    
    def testInsert(self,file):
        self.db.test2_data.delete_many({})
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                columns = line.split(',')
                dic = {}
                for attr in attr_list:
                    element = columns[attr_list.index(attr)]
                    if element.isdigit():
                        element = int(element)
                    elif self.isfloat(element):
                        element = float(element)
                    dic[attr] = element
                print(dic)
                self.db.test2_data.insert_one({"test": dic})



db=Database_Insert()
db.trainInsert("kdd_big.txt")
#db.testInsert("except data/test-1.txt")


