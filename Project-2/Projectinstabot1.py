from selenium import webdriver
import sys
import selenium
# from selenium.webdriver.chrome_driveroptions import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
import datetime
import pandas
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains
import matplotlib.pyplot as plt
import time
from bs4 import BeautifulSoup as bs


chrome_driver = webdriver.Chrome()
actions = ActionChains(chrome_driver)

# Login Function
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

# Function toopen any id
def openid(username):
    # chrome_driver.find_element
    chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").clear()
    chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(username)
    sleep(4)
    chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(Keys.ENTER)
    chrome_driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(Keys.ENTER)



#picture opening function
def first_picture():

	# finds the first picture
    pic=chrome_driver.find_element(By.CLASS_NAME,'_9AhH0')
	# pic = chrome_driver.find_element_by_class_name("kIKUG")
    pic.click() # clicks on the first picture


#picture liking function
def like_pic():
	
    time.sleep(4)
	# like = chrome_driver.find_element_by_class_name('fr66n')
    like=chrome_driver.find_element(By.CLASS_NAME,'fr66n')
	
    soup = bs(like.get_attribute('innerHTML'),'html.parser')
	
    if(soup.find('svg')['aria-label'] == 'Like'):
		
        like.click()
        print('liked')
	
    time.sleep(2)


#scrolling through picture function
def next_picture():
	time.sleep(4)
	try:
		nex = chrome_driver.find_element(By.XPATH,'//div[@class=" l8mY4 feth3"]') 
        # chrome_driver.find_element_by_class_name("coreSpriteRightPaginationArrow")
		time.sleep(1)
		return nex
	except selenium.common.exceptions.NoSuchElementException:
		return 0
count=0

#likes/ dislike function that takes the number of posts to be liked/disliked
def continue_liking(number):
	for i in range(1,number):
		next_el = next_picture()

		# if next button is there then
		if next_el != False:

			# click the next button
			next_el.click()
			time.sleep(4)

			# like the picture
			like_pic()
			time.sleep(4)
            
        


		else:
			print("not found")
			break
# path()
time.sleep(1)


#getting first 10 handles after giving food in search box
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

#gets the first 500 followers
def follower_counter(username):
    openid(username)
    time.sleep(4)
    chrome_driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/main/div/header/section/ul/li[2]/a').click()
    time.sleep(4)
    words=[]
    for i in range(1,20):
        # xpath='/html/body/div[6]/div/div/div[2]/ul/div/li[]/div/div[2]/div[1]/div/div/span/a'
        xpath='/html/body/div[6]/div/div/div[2]/ul/div/li['+str(i)+']'
        time.sleep(1)
        elements=chrome_driver.find_element(By.XPATH,xpath)
        chrome_driver.execute_script("arguments[0].scrollIntoView();", elements)
        # actions.move_to_element(elements).perform()
        string=elements.text
        string=string.split('\n')[0]
        words.append(string)
    return(words)


#tells whether a page has a story or not
def storyteller(ninjas):
    openid(ninjas)
    time.sleep(4)
    element=chrome_driver.find_element(By.XPATH,'/html/body/div[1]/section/main/div/header/div/div')
    text=element.get_attribute('aria-disabled')
    # print(text)
    if text=='true':
        print('No story')
    else:
        element=chrome_driver.find_element(By.XPATH,'/html/body/div[1]/section/main/div/header/div/div/canvas')
        text=element.get_attribute('height')
        if text=='208':
            print('Story seen')
        else:
            print('Story not seen')

# url_name(url)

instalogin('pranshudhyani','Dhy@niPr@n$hu2710')
# openid('Sodelhi')
time.sleep(2)
# first_picture()
# like_pic()
# continue_liking(30)
# followers_list=follower_counter('Sodelhi')
# print(followers_list)
# followers_list=follower_counter('foodtalkindia')
# print(followers_list)
storyteller('cherrywineandcoffeebreath')
# chrome_driver.close()


