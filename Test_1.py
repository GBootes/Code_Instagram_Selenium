from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def Time(t):

    for i in range(0,t):

        a=i

DataLog=open('DataLog.txt','r')
user=DataLog.readline()
passw=DataLog.readline()
   
driver=webdriver.Chrome("C:\Selenium\chromedriver.exe")
driver.get("https://www.instagram.com/accounts/login/")
driver.maximize_window()

driver.find_element_by_name("username").send_keys(user)
ps=driver.find_element_by_name("password").send_keys(passw)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//span[button/@class='_qv64e _gexxb _4tgw8 _njrw0']").click()

driver.find_element_by_xpath("//div[@class='_5ayw3 _ohiyl']/input[1]").send_keys('#TenisAAA')
driver.find_element_by_xpath("//a[@class='_ndl3t']/div[1]").click()

driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]").click()

#Número de Post
numPost=eval(driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/header/div/span/span").get_attribute('innerHTML'))

#Lista nombre de usuarios
userList=[]

for i in range(1,numPost+1):

    if(i==1 or i==numPost+1):

        Time(int(2.5e7))
        #WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[1]/div/div/a"))).click()
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a").click()
        userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))

    else:

        Time(int(2.5e7))
        #WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[1]/div/div/a[2]"))).click()
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a[2]").click()
        userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
