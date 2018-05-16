from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
    #---------------------------------------

    #----------------------Search Hashtag-----------------------------
    #driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div/div").click()
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

            #userList.append(driver.find_element_by_class_name('_2g7d5 notranslate _iadoq').get_attribute('title'))
            userList.append('tenismedellin100')
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a").send_keys(Keys.ARROW_RIGHT)
            time.sleep(1)
            DO.dataOut(file1,userList[i])
            print(i)

        elif(i==numPost-1):

            userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
            DO.dataOut(file1,userList[i])
            print(i)
        
        else:

            userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a[1]").send_keys(Keys.ARROW_RIGHT)
            time.sleep(1)
            DO.dataOut(file1,userList[i])
            print(i)

    users.append(userList[0])

    users=UR.repeat(userList,users,file2)

    post=[]
    followers=[]
    for i in users:
        
        Info=UI.userInfo(i,driver)
        post.append(Info[0])
        followers.append(Info[1])

    driver.quit()
    
    return users,post,followers
########################################################################
#                                 END                                  #
########################################################################

with open('DataLog.txt') as d:

    DataLog=d.read().splitlines()

user=DataLog[0]
passw=DataLog[1]
url=DataLog[2]

profiles=[]
#User,#Password,#URL,#Time_1,#Time_2,#Archive all users,#Archive users,#HashTag
profiles=Search_Profile(user,passw,url,'UserList.txt','UsersNRep.txt','#ventasmedellinonline')

DB=[]
n=len(profiles[0])
for i in range(0,n):

    auxDB=[]
    for j in profiles:

      auxDB.append(j[i])

    DB.append(auxDB)

DBcsv.db(DB)
