from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lxml.html import fromstring
from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
import smtplib,ssl
import time
import shelve
import ctypes
import sys
import threading
import random
from time import sleep


def main():
    port = 465  # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("usernamehere0700@gmail.com", "Smilelily#24")
        server.sendmail("usernamehere0700@gmail.com", "lilydriscoll24@gmail.com", "hi")
if __name__=="__main__":
    main()