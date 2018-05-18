import csv

def db(data,fcsv):
     
    with open(fcsv,'w',newline='') as f:

        w=csv.writer(f)

        w.writerows([['Username','#Post','#Followers','Last_Photo','Phone_1','Biography']])
            
        try:
            
            w.writerows(data)

        except:

            w.writerows(data[0:5])
            print('Error: ',data[0])
