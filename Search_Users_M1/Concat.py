########################################################################
#                           CONCAT FUNCTION                            #
########################################################################
def concat(x):

    k=''
    for i in x:

        k=k+str(i)
    a=''
    
    for i in k:

        if (i.isdigit()):

            a=a+i

    return a