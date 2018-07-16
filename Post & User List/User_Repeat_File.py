import Data_Out as DO
import time

########################################################################
#                           REPEAT USERS                               #
########################################################################
def repeat(fileIn1,fileIn2,fileOut):

    with open(fileIn1) as f1:

        userList=f1.read().splitlines()

    with open(fileIn2) as f2:

        users=f2.read().splitlines()

    print('User List:',len(userList))
    print('Users:',len(users))

    aux=[]
    for i in userList:
    
        s=True
        for k in users:

            if (k==i):

                s=False

        if (s):

            aux.append(i)
            users.append(i)

    print('Users no rep:',len(aux))

    for i in aux:

        DO.dataOut(fileOut,i)
        DO.dataOut(fileIn2,i)
#----------------------------------------------------------------------#
