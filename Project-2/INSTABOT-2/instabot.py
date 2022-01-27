# import pytest
from selenium import webdriver
import sys
import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
import datetime
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas
# import org.openqa.selenium.interactions.Actions
 

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


def profilescrapper():
    chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys('food')
    handles=[]
    for i in range(1,12):
        xpath='/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div['+str(i)+']/a/div/div[2]/div[1]/div/div/div'
        people= chrome_driver.find_element(By.XPATH,xpath).text
        if people=='food' or people=='brfootball':
            continue
        handles.append(people)
        # print(handles)
    return(handles)

def top5(handles):
    dict={}
    for i in handles:
        chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").clear()
        chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(i)
        sleep(4)
        chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(Keys.ENTER)
        chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(Keys.ENTER)
        sleep(4)
        follow=chrome_driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/main/div/header/section/ul/li[2]/a/span')
        followers_count=follow.get_attribute('title')
        followers_count=followers_count.replace(',','')
        dict[i]=followers_count
        x=dict.keys()
        y=dict.values

        sleep(2)
    # print(dict)
    count=0
    d2={}
    while count<=4:
        maxi=0
        for i in dict.keys():
            if int(dict[i])>maxi:
                maxi=int(dict[i])
                pos=i
        d2[pos]=maxi
        del dict[pos]
        count=count+1
    handles=d2.keys()
    # print(d2)
    # color=['Red','Green','Blue','Orange','Cyan']
    # a=d2.keys()
    # b=d2.values()
    # low = min(b)
    # high = max(b)
    # plt.ylim([math.ceil(low-0.5*(high-low)),math.ceil(high+0.5*(high-low))])
    # plt.bar(a,b,width=0.5,color=color)
    # plt.title('Top 5 Handles')
    # plt.xlabel('handles')
    # plt.ylabel('Follower count')
    # plt.show()

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
    # color=['Red','Green','Blue','Orange','Cyan']
    # plt.bar(count,val,width=0.5,color=color)
    # plt.xticks(rotation=40)
    # plt.xlabel('Hashtags')
    # plt.ylabel('Total Occurence')
    # plt.title('Top Hashtags')
    # plt.show()


    print(handles)
    return handles
        

def Timepost(handles):
    val={}
    for k in handles:
        chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").clear()
        chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(k)
        sleep(4)
        chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(Keys.ENTER)
        chrome_driver.find_element(By.XPATH,"/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()
        sleep(4)
        count=0
        for j in range(1,12):
            looper=1
            for i in range(1,4):
                chrome_driver.find_element(By.XPATH,"/html/body/div[1]/div/div/section/main/div/div[3]/article/div[1]/div/div["+str(j)+"]/div["+str(i)+"]/a/div[1]/div[2]").click()
                sleep(4)
                time=chrome_driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/div[2]/a/time').get_attribute('datetime')
                # print(time)
                time=time.split('T')[0]
                # print(time)
                time=time.split('-')[-1]
                # print(time)
                
                # count=count+1
                chrome_driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/button').click()
                if int(time)<=4:
                    looper=0
                    break
                count=count+1
            if looper==0:
                val[k]=count
                break
    return(val)

    
def followlikes(handles):
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
    # color=['Red','Green','Blue','Orange','Cyan']
    # plt.bar(handles,a3,width=0.5,color=color)
    # plt.xticks(rotation=40)
    # plt.xlabel('Handles')
    # plt.ylabel('Ratio in %')
    # plt.title('Likes/Follow ratio')
    # plt.show()

def word_counter(all_word):
    # print(all_word)
    hashtags=[]
    hash=np.array(all_word)
    for i in all_word:
        if '#' in i:
            hashtags.append(i)
    df2=pandas.Series(hashtags)
    df=pandas.Series(all_word)
    word_county=df.value_counts()[0:5]
    Hsh_count=df2.value_counts()[0:5]
    count=word_county.index
    val=word_county.values
    # color=['Red','Green','Blue','Orange','Cyan']
    # plt.bar(count,val,width=0.5,color=color)
    # plt.xticks(rotation=40)
    # plt.xlabel('Hashtags')
    # plt.ylabel('Total Occurence')
    # plt.title('Top Hashtags')
    # plt.show()



instalogin('pranshudhyani','Dhy@niPr@n$hu2710')
# handles=profilescrapper()
# handles=top5(handles)
handles=['yourfoodlab','foodbible','foodie_incarnate','delhifoodwalks','delhi_street_food1']
d=Timepost(handles)
# chrome_driver.close()
