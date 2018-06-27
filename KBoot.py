from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import emoji
import time
import sys
import Login as login
import Concat as Conc
import Data_Out as DO
import User_Repeat as UR
import User_Info as UI
import Next_Post as NPost
import DataBase_csv as DBcsv

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
    numPost=eval(driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div[2]/span/span").get_attribute('innerHTML'))
    
    if (type(numPost)==tuple):

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

    driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]").click()
    time.sleep(2)
    users=[]

    userList=NPost.next(driver,numPost,file1,Keys)
    
    users.append(userList[0])

    users=UR.repeat(userList,users,file2)
    
    print('Users saved')

    post=[]
    followers=[]
    Bio=[]
    Num1=[]
    NumL=[]
    Dateph=[]
    Link=[]
    for user in users:
        
        Info=UI.userInfo(user,driver,emoj)
        post.append(Info[0])
        followers.append(Info[1])
        Dateph.append(Info[2])
        Num1.append(Info[3])
        NumL.append(Info[4])
        Bio.append(Info[5])
        Link.append(Info[6])

    driver.quit()
    
    return users,post,followers,Dateph,Num1,NumL,Bio,Link
########################################################################
#                                 END                                  #
########################################################################

time.clock()
emoj=dict.fromkeys(range(0x1000000, sys.maxunicode + 1), 0xfffd)
with open('DataLog.txt') as d:

    DataLog=d.read().splitlines()

user=DataLog[0]
passw=DataLog[1]
url=DataLog[2]
HT=DataLog[3]

profiles=[]
#User,#Password,#URL,#Time_1,#Time_2,#Archive all users,#Archive users,#HashTag
profiles=Search_Profile(user,passw,url,'UserList.txt','UsersNRep.txt',HT)

DB=[]
n=len(profiles[0])
for i in range(0,n):

    auxDB=[]
    for j in profiles:

      auxDB.append(j[i])

    DB.append(auxDB)

DBcsv.db(DB,'Test.csv')
print(time.clock(),'seconds')
