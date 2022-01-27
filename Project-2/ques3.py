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



def followcounter(handles):
    val={}
    followers=[]
    dict={}
    for k in handles:
        chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").clear()
        chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(k)
        sleep(4)
        chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(Keys.ENTER)
        chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(Keys.ENTER)
        sleep(4)
        count=0
        sum=0
        
        follow=chrome_driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/main/div/header/section/ul/li[2]/a/span')
        followers_count=follow.get_attribute('title')
        followers_count=followers_count.replace(',','')
        dict[k]=followers_count
        followers_count=int(followers_count)
        followers.append(followers_count)
    likes=[154300,18605,40125,4100,5408]
    a1=np.array(followers)
    a2=np.array(likes)
    a3=a2/a1*100
    # print(followers)
    # val=word_county.values
    color=['Red','Green','Blue','Orange','Cyan']
    plt.bar(handles,a3,width=0.5,color=color)
    plt.xticks(rotation=40)
    plt.xlabel('Handles')
    plt.ylabel('Ratio in %')
    plt.title('Likes/Follow ratio')
    plt.show()


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
followcounter(handles)
# print(all_words)
# word_counter(all_words)
