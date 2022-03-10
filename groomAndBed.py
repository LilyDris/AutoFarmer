from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lxml.html import fromstring
from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
import time
import shelve
import ctypes
import sys
import threading
import random
import webbrowser
from time import sleep

def main():
    # set up
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://howrse.com") # Change depending on server
    wait = np.random.uniform(low=1.0, high=2.0, size=50)
    # Clicks refuse cookies
    driver.find_element(by=By.XPATH, value='/html/body/aside/div/article/div/div[2]/div/div/div[2]/form/button').click()
    sleep(np.random.choice(wait))
    driver.find_element(by=By.XPATH, value='/html/body/div[7]/header/nav/div/strong').click()
    sleep(np.random.choice(wait))
    # Logs in
    login = driver.find_element(by=By.ID, value='login')
    login.send_keys("Can't Hold Us") # Change username
    sleep(np.random.choice(wait))
    password = driver.find_element(by=By.ID, value='password')
    password.send_keys("smilelily24") # Change password
    sleep(np.random.choice(wait))
    password.send_keys(Keys.RETURN)
    sleep(5)
    # Goes to specific horse page
    # change this link to where horses reside
    driver.get('https://www.howrse.com/elevage/chevaux/?elevage=1604736') 
    sleep(np.random.choice(wait))
    # Change to path to click on first horse
    driver.find_element(by=By.XPATH,
                        value='/html/body/div[8]/main/section/section/div[2]/div[2]/div[2]/div/div[2]/ul[1]/li[1]/label/div/div[1]/div/ul/li/a').click()  
    sleep(np.random.choice(wait))
    firstVisited= driver.current_url
    print(firstVisited)
    current=""
    while( firstVisited in current):
        wait = np.random.uniform(low=1.0, high=2.0, size=50)
        # Grooms
        driver.find_element(by=By.XPATH, value='/html/body/div[8]/main/section/section/div[4]/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div[1]/a').click()
        sleep(np.random.choice(wait))
        # Puts to bed
        driver.find_element(by=By.XPATH, value='/html/body/div[8]/main/section/section/div[4]/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[1]/a').click()
        sleep(np.random.choice(wait))
        # Clicks next horse
        driver.find_element(by=By.XPATH, value= '/html/body/div[8]/main/section/section/div[4]/div/div[2]/div[1]/div[2]/a[2]').click()
        sleep(np.random.choice(wait))
        current= driver.current_url
        print(current)
        
    driver.close()


if __name__ == "__main__":
    main()
