import Data_Out as DO

########################################################################
#                           REPEAT USERS                               #
########################################################################
def Repeat(fileIn1,fileIn2,fileOut):

    with open(fileIn1) as f1:

        userList=f1.read().splitlines()

    with open(fileIn2) as f2:

        users=f2.read().splitlines()

    for i in userList:
    
        s=True
        for k in users:

            if (k==i):

                s=False

        if (s):

            users.append(i)

    for i in users:

        DO.DataOut(fileOut,i)

    return users
#----------------------------------------------------------------------#
