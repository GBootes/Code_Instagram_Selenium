import Data_Out as DO

########################################################################
#                           REPEAT USERS                               #
########################################################################
def repeat(userList,users,fileOut):

    aux=[]
    for i in userList:
    
        s=True
        for k in users:

            if (k==i):

                s=False

        if (s):

            aux.append(i)
            users.append(i)

    for i in aux:

        DO.dataOut(fileOut,i)
        DO.dataOut('Users.txt',i)

    return users
#----------------------------------------------------------------------#
