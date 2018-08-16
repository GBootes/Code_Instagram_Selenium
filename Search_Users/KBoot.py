from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import Login as login
import Concat as Conc
import Data_Out as DO
import User_Repeat as UR
import Next_Post as NPost

########################################################################
#                           MAIN SEARCH                                #
########################################################################
def Search_Profile(user,passw,url,file1,file2,HT):
    
    driver=login.log(url,user,passw)

    #----------------------Search Hashtag-----------------------------
    driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys(HT)
    time.sleep(2)
    #-----------------------------------------------------------------

    #------------------------Post Number------------------------------
    numPost=driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div[2]/span/span").get_attribute('innerHTML')
    
    if (type(numPost)==tuple):

        numPost=eval(Conc.concat(numPost))

    elif(type(numPost)==float):

        numPost=eval(Conc.concat(str(numPost)))

    elif(type(numPost)==str):

        numPost=eval(Conc.concat(numPost))
        
    print('Total Post:',numPost)
    #-----------------------------------------------------------------

    #--------------------------Close advertising----------------------
    try:

        driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div").click()

    except:

        print('No Advertising')

    time.sleep(2)
    #-----------------------------------------------------------------

    #--------------Initial time------------------
    time_i=time.clock()        
    DO.dataOut('SEARCH_LOG.txt','----SEARCH LOG '+HT+'----')
    DO.dataOut('SEARCH_LOG.txt','INITIAL TIME: '+str(time.ctime()))

    driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]").click()
    time.sleep(2)

    with open('Users.txt','a') as fusers:

        users=fusers.read().splitlines()

    userList=NPost.next(driver,numPost,file1,Keys)

    users=UR.repeat(userList,users,file2)

    time_f=time.clock()
    time4HT=str(abs(time_i-time_f))
    print('Users saved')
    print (time4HT,'seconds','\n','Keyword:',HT)

    DO.dataOut('SEARCH_LOG.txt','FINAL TIME: '+str(time.ctime()))
    DO.dataOut('SEARCH_LOG.txt','TOTAL TIME: '+time4HT+' seconds')
    DO.dataOut('SEARCH_LOG.txt','KEYWORD: '+HT)
    DO.dataOut('SEARCH_LOG.txt','TOTAL POSTS: '+str(len(userList)))
    DO.dataOut('SEARCH_LOG.txt','TOTAL USERS: '+str(len(users)))
    DO.dataOut('SEARCH_LOG.txt','\n')
    DO.dataOut('SEARCH_LOG.txt','----------------------------------------')
    DO.dataOut('SEARCH_LOG.txt','\n')
    
    driver.quit()
    
    return users
########################################################################
#                                 END                                  #
########################################################################

time.clock()
emoj=dict.fromkeys(range(0x1000000, sys.maxunicode + 1), 0xfffd)
with open('DataLog.txt') as d:

    DataLog=d.read().splitlines()

with open('KeyWords.txt') as kw:

    keywords=kw.read().splitlines()

n=len(keywords)

user=DataLog[0]
passw=DataLog[1]
url=DataLog[2]

Users=[]
for i in range(n):

    file1='PostList_X('+keywords[i]+'_x).txt'
    file2='UsersNRep_'+keywords[i]+'_x).txt'

    Users.append(Search_Profile(user,passw,url,file1,file2,keywords[i]))
