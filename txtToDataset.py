from io import open
from Category import *
from Mongo_connection import *


def transform_type(input_file, output_file):
    with open(output_file, "w") as text_file:
        with open(input_file) as f:
            lines = f.readlines()
            cnt=0
            for line in lines:
                if cnt!=0:
                    
                    line=line.replace('\t',',')
                    columns = line.split(",")
                    columns.pop(0)
                    #print(len(columns))
                    print(columns)
                    
                    for raw_type in category:
                        flag = False
                        if raw_type == columns[-1].replace("\n", " "):
                            str = ','.join(columns[0:attr_list.index('type')])
                            print(str)
                            text_file.write("%s,%d\n" % (str, category[raw_type]))
                            flag = True
                            break
                    if not flag:
                        text_file.write(line)
                        print(line)
                cnt+=1
                
def type_alott(input_file,output_file):
    with open(output_file,"w") as out:
        with open(input_file) as f:
            lines =f.readlines()
            
            for line in lines:
                line=line.replace('\n',',')
                columns=line.split(',')
                columns.pop()
                
                print(columns)
                columns[-1]=str(category[columns[-1]+'.'])
                line=""
                for x in range(0,len(columns)-1) :
                    line=line + str(columns[x]) +','
                line =line + columns[-1]
                
                out.write("%s\n"% (line))
                print(line)


def transform_type_except_data(input_file, output_file):
    with open(output_file, "w") as text_file:
        with open(input_file) as f:
            lines = f.readlines()
            cnt=0
            for line in lines:
                if cnt!=0:
                    
                    line=line.replace('\t',',')
                    columns = line.split(",")
                    columns.pop(0)
                    #print(len(columns))
                    print(columns)
                    columns[-1]=columns[-1].replace('\n','.')
                    columns[-1]=str(category[columns[-1]])
                    stre=','.join(columns)
                    print(stre)
                    text_file.write("%s\n" % (stre))
                    
                    
                    
                    
                cnt+=1
#type_alott('target1.txt','target_data.txt')

transform_type_except_data('test.txt','test-1.txt')