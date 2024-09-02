# -*- coding: utf-8 -*-
from __future__ import print_function
from selenium import webdriver
import requests
import random
from bs4 import BeautifulSoup
import soupsieve
import pickle
import os
from os.path  import basename
import re
# import short_ids
from short_ids import short_id_arr
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

short_id_url = "https://www.intanibase.com/iad_entries/screenshots?shortID="
masthead_element = 'div[class="masthead_inner"]'
img_element = 'img[class="screenshot_thumb"]'
masthead_span_id_bad = 'span[id="ctl00_iadb_v2_cph_masthead_create_header_LBL_Title"]'
masthead_span_id_good = 'span[id="ctl00_ctl00_iadb_v2_cph_masthead_ctl00_LBL_Header"]'


# Trying the dummy way first, just iterate through shortID numbers up to like 10000 -> if there are no screenshots try the next URL 
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'fc-button-label'))
    )
    element.click()


    # look at the last number stored in some list stored locally 
    last_known_id = 10000
    while last_known_id < 20000:
        print(f'Currently navigating to ID #: {last_known_id}')
        r = driver.get(f'{short_id_url}{last_known_id}')        
        # print(r)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, masthead_element)))
        # Click out of any ads ("#mys-content #dismiss-button") (or maybe you can just click the body ? not sure with selenium)
        html = driver.page_source
        soup = BeautifulSoup(html, features="html.parser")
        # soup = BeautifulSoup(r.text, "html.parser")
        good_title = soup.select_one(masthead_span_id_good)

        if good_title != None:
            title_str = good_title.text.strip()
            cleaned_title = re.sub(r'[^a-zA-Z0-9\s]', '', title_str)
            print(f'the title is: {cleaned_title}')
        else: 
            print(f'detected title mismatch, got: {good_title}')
        
        # find screenshots and write them to directory
        for link in soup.select(img_element):
            # check to see if the cartoon was made before 1988
            release_year = soup.select_one(f'span[id*="Release"]').text
            cleaned_release_year = release_year[-4:]
            release_year_int = int(cleaned_release_year)

            if release_year_int < 1989:
                # new way
                lnk = link["src"]
                img_data = requests.get(lnk).content
                cleaned_file_name = re.sub(r'[^a-zA-Z0-9\s]', '', f'{last_known_id}-{lnk}')
                new_file_path = os.path.join("screenshots", cleaned_file_name + '.jpg')
                with open(new_file_path, 'wb') as handler:
                    handler.write(img_data)
            
            # old way
            # lnk = link["src"]
            # with open(f'screenshots/{last_known_id}-{lnk}'," w") as f:
            #     f.write(requests.get(lnk).content)
        last_known_id +=1

    # starting there, go to that shortID url
    # wait
    # check for a title element that isn't "Title Error"
    # if so, grab that and store it temporarily as the title of the show 
    # grab the series and release date strings and store those too 
    # strip down all of the strings so they dont have quotes and stuff
    # iterate through all the screenshot images, for each one write it to the screenshots dir with the format "show-date-title-number"
    # when done with that episode, push the shortID to the list stored locally and complete the loop 
finally:
    # quit
    # driver.quit()
    print('uh oh!!!')




# ***** TO TRY LATER // MORE GRACEFUL *****


# # Store the animator,year values to dict in local 
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, 'ctl00$iadb_v2_cph_maincontent$DDL_Studios'))
#     )
#     # read through all of the animators right off the bat -> store as the initial k,v pair -> the first value can just be "name"
#     # for each animator
#     # click the animator name
#     # wait until page reloads
#     # read all of the years, filter through and only include everything before 1995
#     element.click()
# finally:
#     # quit
#     driver.quit()

# # Actually grab the screenshots - you should probably duplicate the master k,v set just for safe keeping once it's formatted properly 
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, 'ctl00$iadb_v2_cph_maincontent$DDL_Studios'))
#     )
#     # Look at the animators dict
#     # Starting with the first animator, check to see if there are any years associated -> if not, delete that animator from k,v pairs and move on
#     # click that animator
#     # wait
#     # iterating through the years,
#     # click that year
#     # wait
#     # grab all of the episode names, strip them of special characters, quotes, etc. and store in a temporary dict/list
#     # iterate through list and check to see if there are any episodes that don't exists as directories within screenshots/animator/year/episode
#     # if not, make that missing episode directory
#     # click on that episode
#     # wait
#     # store screenshots in episode path dir
#     # delete that episode from temp storage
#     # upon completion, delete the year from the k,v pair

#     # given that we're checking to see if there are any year keys, we should be able to detect
#     element.click()
# finally:
#     # quit
#     driver.quit()