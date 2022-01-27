from selenium import webdriver
import sys
import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
import datetime
import pandas
import numpy as np
import matplotlib.pyplot as plt


chrome_driver = webdriver.Chrome()
def instalogin(username,password):    
    chrome_driver.get('https://www.instagram.com/')
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(4)
    a=chrome_driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")

    a.send_keys(username)
    chrome_driver.implicitly_wait(2)
    chrome_driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(password)

    chrome_driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button").click()
    # chrome_driver.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/div/div/div/button").click()
    sleep(3)
    chrome_driver.find_element(By.XPATH,"//button[contains(text(),'Not Now')]").click()
    sleep(3)
    chrome_driver.find_element(By.XPATH,"//button[contains(text(),'Not Now')]").click()



def postscrapper(handles):
    val={}
    all_words=[]
    for k in handles:
        chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").clear()
        chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(k)
        sleep(4)
        chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(Keys.ENTER)
        chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(Keys.ENTER)
        sleep(4)
        count=0
        
        for j in range(1,5):
            looper=1
            for i in range(1,4):
                chrome_driver.find_element(By.XPATH,"/html/body/div[1]/div/div/section/main/div/div[3]/article/div[1]/div/div["+str(j)+"]/div["+str(i)+"]/a/div[1]/div[2]").click()
                sleep(4)
                words=chrome_driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/span').text
                # print(time)
                # print(words)
                w=words.split(' ')
                all_words.extend(w)
                # print(time)
                # time=time.split('-')[-1]
                # print(time)
                
                # count=count+1
                chrome_driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/button').click()
                # if int(time)<=4:
        #             # looper=0
        #             break
        #         count=count+1
        #     if looper==0:
        #         val[k]=count
        #         break
        # print(val)
    return(all_words)

def word_counter(all_word):
    # print(all_word)
    hashtags=[]
    hash=np.array(all_word)
    for i in all_word:
        if '#' in i:
            hashtags.append(i)
    df2=pandas.Series(hashtags)
    df=pandas.Series(all_words)
    word_county=df.value_counts()[0:5]
    Hsh_count=df2.value_counts()[0:5]
    count=word_county.index
    val=word_county.values
    color=['Red','Green','Blue','Orange','Cyan']
    plt.bar(count,val,width=0.5,color=color)
    plt.xticks(rotation=40)
    plt.xlabel('Hashtags')
    plt.ylabel('Total Occurence')
    plt.title('Top Hashtags')
    plt.show()

    # print(df2)
    
instalogin('pranshudhyani','Dhy@niPr@n$hu2710')
# handles=profilescrapper()
# handles=top5(handles)
handles=['yourfoodlab','foodbible','foodie_incarnate','delhifoodwalks','delhi_street_food1']
all_words=postscrapper(handles)
# print(all_words)
word_counter(all_words)
