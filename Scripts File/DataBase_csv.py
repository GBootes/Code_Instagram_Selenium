import csv
import sys

def db(data,fcsv):

    aux=[]
    with open(fcsv,'w',newline='') as f:

        w=csv.writer(f)

        w.writerows([['nombre','no_publicaciones','no_seguidores','fecha_ult_pub','tel1','tel2','tel3','bio', 'link','keyword']])

        k=1
        for i in data:

            aux.append(i)
            try:

                w.writerows(aux)

            except:

                print(k,'Error:',sys.exc_info()[0])

            aux=[]
            k=k+1
