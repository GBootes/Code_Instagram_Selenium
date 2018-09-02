import time
import sys
import Data_Out as DO

def next(driver,numPost,file1,Keys):

     userList=[]
     i=0
     dt=2018
     while (i<numPost and dt>2016):

          try:
               if (i>8):
                    
                    dt=''
                    dtp=driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/div[2]/div[2]/a/time").get_attribute('datetime')

                    for k in range(0,4):

                         dt=dt+dtp[k]
               
                    dt=eval(dt)

          except:

               print('Date no available')

          if (i==0):
               
               try:
                    
                    userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
                    DO.dataOut(file1,userList[i])
                    time.sleep(1)
                    driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a").click()
               except:

                    userList.append('tenismedellin100')
                    DO.dataOut(file1,userList[i])
                    print (i+1,"Unexpected error:", sys.exc_info()[0])
                    time.sleep(1)

          elif (i==numPost-1):
               
               try:

                    userList.append(driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a").get_attribute('title'))
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
                    DO.dataOut(file1,userList[i])
                    time.sleep(1)
                    driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a[2]").send_keys(Keys.ARROW_RIGHT)
               except:

                    try:
                         driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/a[2]").send_keys(Keys.ARROW_RIGHT)
                         userList.append('tenismedellin100')
                         DO.dataOut(file1,userList[i])
                    except:

                         print (i+1,"Unexpected error:", sys.exc_info()[0])
                         i=numPost
                    
          i+=1

     print ('End sweep')
          
     return userList
