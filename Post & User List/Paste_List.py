import Data_Out as DO

def pastelist(file1,file2,file3,file4,fileOut):

     with open(file1) as f1:

          u1=f1.read().splitlines()

     with open(file2) as f2:

          u2=f2.read().splitlines()

     with open(file3) as f3:

          u3=f3.read().splitlines()

     with open(file4) as f4:

          u4=f4.read().splitlines()

     u=u1+u2+u3+u4

     for i in u:

        DO.dataOut(fileOut,i)
