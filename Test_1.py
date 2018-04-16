from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import Time as T
import Concat as C
import Data_Out as DO
import User_Repeat as UR

########################################################################
#                           CONCAT FUNCTION                            #
########################################################################
def Concat(x):

    k=""
    for i in x:

        k=k+str(i)

    return k
#----------------------------------------------------------------------#

########################################################################
#                      EXTERNAL FILE WITH USERS                        #
########################################################################   
def Data_Out(file,x):
    
    DataOut=open(file,'a')
    DataOut.write(x)
    DataOut.write('\n')
    DataOut.close
#----------------------------------------------------------------------#

########################################################################
#                           REPEAT USERS                               #
########################################################################
def User_Repeat(userList,users,file2):

    for i in userList:
    
        s=True
        for k in users:

            if (k==i):

                s=False

        if (s):

            users.append(i)

    for i in users:

        Data_Out(file2,i)

    return users
#----------------------------------------------------------------------#

########################################################################
#                           MAIN SEARCH                                #
########################################################################
def Search_Profile(user,passw,url,t1,t2,file1,file2,HT):
    
    driver=webdriver.Chrome("C:\Selenium\chromedriver.exe")
    driver.get(url)
    driver.maximize_window()

    userField=driver.find_element_by_name("username").send_keys(user)
    passField=driver.find_element_by_name("password").send_keys(passw)
    logBtn=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/span/button").click()
    T.time(int(eval(t1)))
    
    driver.get('https://www.instagram.com/')
    
    driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div/div").click()
    driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys(HT)
    
    T.time(int(eval(t1)))
    driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div").click()
    T.time(int(eval(t1)))

    #Número de Post
    numPost=eval(driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/header/div/span/span").get_attribute('innerHTML'))
    print(numPost)

    if (type(numPost)==tuple):
        
        numPost=eval(Concat(numPost))
        
    print(numPost)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]").click()

    #Lista nombre de usuarios
    userList=[]
    users=[]

    for i in range(numPost):

        print(i)

        if(i==0):
    
            userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
            print(userList[i])
            T.time(int(eval(t1)))
            driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a").click()
            T.time(int(eval(t2)))
            Data_Out(file1,userList[i])

        elif(i==numPost-1):

            userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
            Data_Out(file1,userList[i])
        
        else:

            userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
            T.time(int(eval(t1)))
            driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a[2]").click()
            T.time(int(eval(t2)))
            Data_Out(file1,userList[i])

    driver.quit()

    users.append(userList[0])

    users=User_Repeat(userList,users,file2)

    return users
#----------------------------------------------------------------------#

with open('DataLog.txt') as d:

    DataLog=d.read().splitlines()

user=DataLog[0]
passw=DataLog[1]
url=DataLog[2]
t1=DataLog[3]
t2=DataLog[4]

profiles=[]
#User,#Password,#URL,#Time_1,#Time_2,#Archive all users,#Archive users,#HashTag
profiles=Search_Profile(user,passw,url,t1,t2,'UserList.txt','UsersNRep.txt','#CamiloFerrer')
