########################################################################
#                      EXTERNAL FILE WITH USERS                        #
########################################################################   
def dataOut(file,x):
    
    DataOut=open(file,'a')
    DataOut.write(x)
    DataOut.write('\n')
    DataOut.close
#----------------------------------------------------------------------#
