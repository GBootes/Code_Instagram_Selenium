from selenium.webdriver.common.keys import Keys
import time
import Delete_Emoji as DE
import Number

def userInfo(user,driver,emoj):
    
    url='https://www.instagram.com/'+user
    driver.get(url)

    time.sleep(1)
    post=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span").get_attribute('innerHTML')
    followers=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").get_attribute('innerHTML')
    #Biography
    try:
        bio=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[2]/span/span").text
        bio=bio.translate(emoj)
        bio=DE.without_emoji(bio)

    except:

        bio='No biography'

    num=Number.num(bio)

    #Last Photo
    try:

        lastph=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div/h2").get_attribute('innerHTML')

    except:

        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div[1]/div/div[1]/div[1]/a/div/div[2]").click()
        time.sleep(2)
        lastph=driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/article/div[2]/div[2]/a/time").get_attribute('title')

    return post,followers,lastph,num,bio
