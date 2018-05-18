from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import emoji
import time
import sys
import User_Info as UI
import DataBase_csv as DBcsv

emoj=dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

with open('DataLog.txt') as d:

    DataLog=d.read().splitlines()

user=DataLog[0]
passw=DataLog[1]
url=DataLog[2]

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
#----------------------------------------------------------------

########################################################################
#                           USER INFO                                  #
########################################################################
def u_info(users):

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

    return post,followers,Dateph,Num,Bio
########################################################################
#                                 END                                  #
########################################################################

time.clock()

with open('UsersNRep.txt') as u:

    users=u.read().splitlines()

profiles=u_info(users)
profiles=(users,)+profiles

DB=[]
n=len(profiles[0])
for i in range(0,n):

    auxDB=[]
    for j in profiles:

      auxDB.append(j[i])

    DB.append(auxDB)

DBcsv.db(DB,'DB_report.csv')
print(time.clock(),'seconds')
