from selenium import webdriver
import Data_Out as DO

def BioProfile(url):

    driver=webdriver.Chrome("C:\Selenium\chromedriver.exe")
    driver.get(url)
    driver.maximize_window()

    dbio=driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/header/section/div[2]/span/span").text
    driver.close()
    return dbio

with open('LinksTest.txt') as dt:

    users=dt.read().splitlines()

links=[]
k=0
#for i in users:
    
    #links.append('https://www.instagram.com/'+i)
    #DO.DataOut('Links.txt',links[k])
    #k=k+1

for i in users:

    DO.DataOut('Bio.txt',BioProfile(i))
