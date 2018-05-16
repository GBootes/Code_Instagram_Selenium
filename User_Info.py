import time

def userInfo(user,driver):
    
    url='https://www.instagram.com/'+user
    driver.get(url)

    time.sleep(1)
    post=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span").get_attribute('innerHTML')
    followers=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").get_attribute('innerHTML')
    
    return post,followers
