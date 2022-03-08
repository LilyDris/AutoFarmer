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

    # url = "https://us.howrse.com/elevage/chevaux/?elevage=all-horses"
    # chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    # driver = webdriver.Chrome('./chromedriver')
    # driver.get(url)
    # driver.close()
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://us.howrse.com")
    print(driver.title)
    login = driver.find_element(by=By.NAME, value='login')
    login.clear()
    login.send_keys("Blubbery")
    driver.find_element(by=By.CLASS_NAME,value='btn--secondary btn form__submit button button-style-submit').click()
    password = driver.find_element(by=By.CLASS_NAME, value='password')
    password.clear()
    password.send_keys("smilelily24")
    password.send_keys(Keys.RETURN)
    print(driver.current_url)
    driver.close()


if __name__ == "__main__":
    main()
