import csv

def db(myData):
     
    myFile = open('DB_1.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)
     
