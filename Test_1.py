from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def Time(t):

    for i in range(0,t):

        a=i
        
def Data_Out(file,x):
    
    DataOut=open(file,'a')
    DataOut.write(x)
    DataOut.close
    

DataLog=open('DataLog.txt','r')
user=DataLog.readline()
passw=DataLog.readline()
url=DataLog.readline()
t1=DataLog.readline()
t2=DataLog.readline()
   
driver=webdriver.Chrome("C:\Selenium\chromedriver.exe")
driver.get(url)
driver.maximize_window()

userField=driver.find_element_by_name("username").send_keys(user)
passField=driver.find_element_by_name("password").send_keys(passw)
driver.implicitly_wait(10)
logBtn=driver.find_element_by_xpath("//span[button/@class='_qv64e _gexxb _4tgw8 _njrw0']").click()
#driver.find_element_by_name("username").send_keys(user)
#driver.find_element_by_name("password").send_keys(passw)
#driver.implicitly_wait(10)
#driver.find_element_by_xpath("//span[button/@class='_qv64e _gexxb _4tgw8 _njrw0']").click()

driver.find_element_by_xpath("//div[@class='_5ayw3 _ohiyl']/input[1]").send_keys('#camiloferrer')
driver.find_element_by_xpath("//a[@class='_ndl3t']/div[1]").click()

#Número de Post
numPost=eval(driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/header/div/span/span").get_attribute('innerHTML'))

driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]").click()

#Lista nombre de usuarios
userList=[]
users=[]

for i in range(numPost):

    if(i==0):

        #WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[1]/div/div/a"))).click()
        userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
        Time(int(eval(t1)))
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a").click()
        Time(int(eval(t2)))
        Data_Out('Users.txt',userList[i])

    elif(i==numPost-1):

        userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
        Data_Out('Users.txt',userList[i])
        
    else:

        #WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[1]/div/div/a[2]"))).click()
        userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
        Time(int(eval(t1)))
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a[2]").click()
        Time(int(eval(t2)))
        Data_Out('Users.txt',userList[i])

users.append(userList[0])

for i in userList:
    
    s=True
    for k in users:

        if (k==i):

            s=False

    if (s):

        users.append(i)