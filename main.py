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


def find_feed_amount(driver):
    feed = driver.find_element(by=By.XPATH, value='//*[@id="feeding"]/table[1]/tbody/tr[2]/td[1]/span[2]/strong').text
    oats = driver.find_element(by=By.CLASS_NAME, value='section-avoine section-avoine-target').text
    print(feed, " ", oats)


def needs_feed(driver):
    need = True
    nursing = driver.find_element(by=By.XPATH, value='//*[@id="boutonAllaiter"]/span').text
    if nursing == 'Nurse':
        need = False
    print(need)


def main():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://us.howrse.com")
    print(driver.title)
    wait = np.random.uniform(low=1.0, high=2.0, size=50)
    driver.find_element(by=By.XPATH, value='/html/body/aside/div/article/div/div[2]/div/div/div[2]/form/button').click()
    sleep(np.random.choice(wait))
    driver.find_element(by=By.XPATH, value='/html/body/div[7]/header/nav/div/strong').click()
    sleep(np.random.choice(wait))
    login = driver.find_element(by=By.ID, value='login')
    login.send_keys("Blubbery")
    sleep(np.random.choice(wait))
    password = driver.find_element(by=By.ID, value='password')
    password.send_keys("smilelily24")
    sleep(np.random.choice(wait))
    password.send_keys(Keys.RETURN)
    sleep(5)
    driver.get('https://us.howrse.com/elevage/chevaux/?elevage=all-horses')  # Goes to all horse page
    sleep(np.random.choice(wait))
    driver.find_element(by=By.XPATH,
                        value='/html/body/div[7]/main/section/section/div[1]/div[2]/div[2]/div/div[2]/ul/li[1]/div/div[1]/div/ul/li/a').click()  # CLicks on first horse
    sleep(np.random.choice(wait))
    for x in range(3):
        wait = np.random.uniform(low=1.0, high=5.0, size=50)
        # driver.find_element(by=By.XPATH,
        # value='/html/body/div[7]/main/section/section/div[4]/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div[1]/a').click()  # Clicks on Groom
        # sleep(np.random.choice(wait))
        if (needs_feed(driver)):
            find_feed_amount(driver)
            sleep(np.random.choice(wait))
        else:
            print(needs_feed(driver))
            sleep(np.random.choice(wait))
        driver.find_element(by=By.XPATH,
                            value='/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]').click()
        sleep(np.random.choice(wait))

    driver.close()


if __name__ == "__main__":
    main()
