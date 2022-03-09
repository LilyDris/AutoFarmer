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

    wait=np.random.uniform(low=1.0,high=5.0,size=20)
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://us.howrse.com")
    print(driver.title)
    driver.find_element(by=By.XPATH, value="/html/body/aside/div/article/div/div[2]/div/div/div[2]/form/button").click()
    sleep(np.random.choice(wait))
    driver.find_element(by=By.XPATH, value="/html/body/div[7]/header/nav/div/strong").click()
    sleep(np.random.choice(wait))
    login = driver.find_element(by=By.ID, value='login')
    login.send_keys("Blubbery")
    sleep(np.random.choice(wait))
    password = driver.find_element(by=By.ID, value='password')
    password.send_keys("smilelily24")
    sleep(np.random.choice(wait))
    password.send_keys(Keys.RETURN)
    sleep(5)
    driver.get('https://us.howrse.com/elevage/chevaux/?elevage=all-horses')
    sleep(np.random.choice(wait))
    print(driver.current_url)
    driver.close()


if __name__ == "__main__":
    main()
