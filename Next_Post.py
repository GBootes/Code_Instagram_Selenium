import time
import sys
import Data_Out as DO

def next(driver,numPost,file1,Keys):

     userList=[]
     i=0
     while i<numPost:

          if (i==0):
               
               try:
                    
                    userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
                    time.sleep(1)
                    DO.dataOut(file1,userList[i])
                    time.sleep(1)
                    print(i+1,userList[i])
                    driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a").click()
                    time.sleep(1)                    
               except:

                    userList.append('tenismedellin100')
                    DO.dataOut(file1,userList[i])
                    print (i+1,"Unexpected error:", sys.exc_info()[0])
                    time.sleep(1)

          elif (i==numPost-1):
               
               try:

                    userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
                    time.sleep(1)
                    print(i+1,userList[i])
                    DO.dataOut(file1,userList[i])
                    time.sleep(1)
               except:

                    userList.append('tenismedellin100')
                    DO.dataOut(file1,userList[i])
                    print (i+1,"Unexpected error:", sys.exc_info()[0])
                    time.sleep(1)

          else:

               try:

                    userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
                    time.sleep(1)
                    DO.dataOut(file1,userList[i])
                    time.sleep(1)
                    print(i+1,userList[i])
                    driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a[2]").send_keys(Keys.ARROW_RIGHT)
                    time.sleep(1)
               except:

                    try:
                         driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a[2]").send_keys(Keys.ARROW_RIGHT)
                         time.sleep(1)
                         userList.append('tenismedellin100')
                         time.sleep(1)
                         DO.dataOut(file1,userList[i])
                         print(i+1,userList[i])
                    except:

                         print (i+1,"Unexpected error:", sys.exc_info()[0])
                         i=numPost
                    
          i+=1

     print ('End sweep')
          
     return userList
