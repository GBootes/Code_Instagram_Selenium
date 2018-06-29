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
    #print('Post:', post)

    #Followers
    followers=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").get_attribute('title')
    #print('Followers:',followers)
    
    #Biography
    try:
                                     
        bio=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[2]/span").get_attribute('innerHTML')
        bio=bio.translate(emoj)
        bio=DE.without_emoji(bio)
        #print('Biography:',bio)

    except:

        bio='No biography'
        #print('Biography:',bio)

    #Link
    try:

        link=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[2]/a").get_attribute('innerHTML')
        #print('Link:',link)

    except:

        link='No link'
        #print('Link:',link)


    #Number
    Nums=Number.num(bio)
    #print('Numbers:',Nums)
    num1=Nums[0]
    num2=Nums[1]
    numsL=Number.num(link)
    numL=numsL[0]
    #print('Number Link:',numL)

    #Last Photo
    try:
                                     
        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/article/div[1]/div/div[1]/div[1]/a/div").click()
        time.sleep(2)        
        lastph=driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/div[2]/div[2]/a/time").get_attribute('title')
        #print('Last photo',lastph)      
        
    except:

        lastph='Private Account'
        #print('Last photo',lastph)

    if (numL==num1 or numL==num2):

        numL=''

    return post,followers,lastph,num1,num2,numL,bio,link
