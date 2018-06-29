import Data_Out as DO

########################################################################
#                           REPEAT USERS                               #
########################################################################
def repeat(userList,users,fileOut):

    for i in userList:
    
        s=True
        for k in users:

            if (k==i):

                s=False

        if (s):

            users.append(i)

    for i in users:

        DO.dataOut(fileOut,i)

    return users
#----------------------------------------------------------------------#
