from selenium import webdriver
import time

def log(url,user,passw):
    
    #-----------Open Instagram Web Site--------------------
    driver=webdriver.Chrome("C:\Selenium\chromedriver.exe")
    driver.get(url)
    driver.maximize_window()
    #------------------------------------------------------

    #-----------------------User Login-------------------------------
    userField=driver.find_element_by_name("username").send_keys(user)
    passField=driver.find_element_by_name("password").send_keys(passw)                                        
    logBtn=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/button").click()
    time.sleep(3)
    #----------------------------------------------------------------

    #------------Refresh page---------------
    driver.get('https://www.instagram.com/')
    time.sleep(2)

    try:

        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/button[2]").click()
    except:

        print('No Notifications')
    
    try:
        
        driver.find_element_by_xpath("//*[@id='react-root']/section/div/span").click()
    except:
        print('No Advertising')
    #---------------------------------------

    return driver
