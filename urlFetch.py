# -*- coding: utf-8 -*-
from __future__ import print_function
from selenium import webdriver
import requests
import random
from bs4 import BeautifulSoup
import soupsieve
import os
import re
import urls
from core_urls import urlArr
import videoparts
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

print("\nRUNNING\n")

#PhantomJS
options = Options()
# options.add_argument('-headless')
driver = Firefox()
wait = WebDriverWait(driver, timeout=10)
driver.get('https://www.intanibase.com/iad_screenshots/index.aspx')


# select the animator 
element = driver.find_element(By.CLASS_NAME, 'nav_bar_new select option[value="8"]')
element.click()

driver.implicitly_wait(5)

element = driver.find_element(By.CLASS_NAME, 'nav_bar_new select option[value="8"]')
element.click()

driver.quit()

# select the year 

# select an episode

# click screenshots

# download photos 

# repeat
