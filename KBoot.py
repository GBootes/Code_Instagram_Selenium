from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import emoji
import time
import sys
import Concat as Conc
import Data_Out as DO
import User_Repeat as UR
import User_Info as UI
import DataBase_csv as DBcsv

########################################################################
#                           MAIN SEARCH                                #
########################################################################
def Search_Profile(user,passw,url,file1,file2,HT):

    #-----------Open Instagram Web Site--------------------
    driver=webdriver.Chrome("C:\Selenium\chromedriver.exe")
    driver.get(url)
    driver.maximize_window()
    #------------------------------------------------------

    #-----------------------User Login-------------------------------
    userField=driver.find_element_by_name("username").send_keys(user)
    passField=driver.find_element_by_name("password").send_keys(passw)
    logBtn=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/span/button").click()
    time.sleep(1)
    #----------------------------------------------------------------

    #------------Refresh page---------------
    driver.get('https://www.instagram.com/')
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div/span").click()
    #---------------------------------------

    #----------------------Search Hashtag-----------------------------
    driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys(HT)
    time.sleep(2)
    #-----------------------------------------------------------------

    #------------------------Post Number------------------------------
    numPost=eval(driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div[2]/span/span").get_attribute('innerHTML'))
    
    if (type(numPost)==tuple):

        numPost=eval(Conc.concat(numPost))
        
    driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div").click()
    time.sleep(2)
    #------------------------------------------------------------------

    driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]").click()
    userList=[]
    users=[]

    for i in range(numPost):

        if(i==0):

            try:

                userList.append(driver.find_element_by_class_name('_2g7d5 notranslate _iadoq').get_attribute('title'))
                time.sleep(1)
                driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a").send_keys(Keys.ARROW_RIGHT)
                time.sleep(1)
                DO.dataOut(file1,userList[i])

            except:

                userList.append('tenismedellin100')
                DO.dataOut(file1,userList[i])

        elif(i==numPost-1):

            try:

                userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
                DO.dataOut(file1,userList[i])

            except:

                userList.append('tenismedellin100')
                DO.dataOut(file1,userList[i])
        
        else:

            try:

                userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
                time.sleep(1)
                driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a[1]").send_keys(Keys.ARROW_RIGHT)
                time.sleep(1)
                DO.dataOut(file1,userList[i])

            except:

                userList.append('tenismedellin100')
                DO.dataOut(file1,userList[i])

    users.append(userList[0])

    users=UR.repeat(userList,users,file2)

    post=[]
    followers=[]
    Bio=[]
    Num=[]
    Dateph=[]
    for user in users:
        
        Info=UI.userInfo(user,driver,emoj)
        post.append(Info[0])
        followers.append(Info[1])
        Dateph.append(Info[2])
        Num.append(Info[3])
        Bio.append(Info[4])

    driver.quit()
    
    return users,post,followers,Dateph,Num,Bio
########################################################################
#                                 END                                  #
########################################################################

time.clock()
emoj=dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
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

DBcsv.db(DB,'DB.csv')
print(time.clock(),'seconds')
