from selenium.webdriver.common.keys import Keys
import time
import Delete_Emoji as DE
import Number

def userInfo(user,driver,emoj):
    
    url='https://www.instagram.com/'+user
    driver.get(url)

    time.sleep(1)
    #Posts
    post=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span").get_attribute('innerHTML')

    #Followers
    followers=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").get_attribute('title')

    #Biography
    try:
        
        bio=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[2]/span[1]").text
        bio=bio.translate(emoj)
        bio=DE.without_emoji(bio)

    except:

        bio='No biography'

    #Link
    try:

        link=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[2]/a").get_attribute('innerHTML')

    except:

        link='No link'


    #Number
    Nums=Number.num(bio)
    num1=Nums[0]
    num2=Nums[1]
    numsL=Number.num(link)
    numL=numsL[0]

    #Last Photo
    try:

        lastph=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div/h2").get_attribute('innerHTML')
        lastph='Private Account'
        
    except:

        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div[1]/div/div[1]/div[1]/a/div/div[2]").click()
        time.sleep(2)        
        lastph=driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/div[2]/div[2]/a/time").get_attribute('title')

    if (numL==num1 or numL==num2):

        numL=''

    return post,followers,lastph,num1,num2,numL,bio,link
