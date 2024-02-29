#!/usr/bin/env python3

# Imports
import json
import time
import random


import file_io
import proxy
from generate_survey_responses import generate_response
from file_io import clean_file
from proxy import getProxyList

from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import config.config as conf
from survey_logic import take_survey, clickNext



session_count = 0
# this bot can complete surveys as the speed of sound.
# however, mcdonalds rightly suspects that it might not be a human doing it
# so we have to throttle it.


MINUTES_PER_HOUR = 60
SECONDS_PER_HOUR = MINUTES_PER_HOUR * 60
SECONDS_PER_SURVEY = SECONDS_PER_HOUR / conf.SURVEYS_PER_HOUR
STEPS_PER_SURVEY = 15
SECONDS_PER_STEP = SECONDS_PER_SURVEY / STEPS_PER_SURVEY
SECONDS_DELAY = SECONDS_PER_STEP
print(f"surveys should take approximately {SECONDS_PER_SURVEY} seconds.")

PROXY_FILE_PATH = "TextFiles/proxyServers.txt"
WINDOW_SIZE = "1920,1080"
STARTING_PROXY = 0 #0-9
COUNT = 0



if __name__ == "__main__":

    # reads codes from file, remove blank lines
    if conf.IS_TEST_MODE:
        code_file_path = ".TextFiles/testCodes.txt"
        print("Running in test mode...")
    else:
        code_file_path = "TextFiles/codes.txt"
        print("Running...")

    clean_file(code_file_path)
    print("loading codes from file.")
    RECEIPT_CODES = file_io.copy_file_to_array(code_file_path)
    PROXY_LIST = file_io.copy_file_to_array(PROXY_FILE_PATH)
    # Here is a convenient list for slicing
    options = ["Opt5", "Opt4", "Opt3", "Opt2", "Opt1"]

    while RECEIPT_CODES:
        code = RECEIPT_CODES.pop(0)
        proxyServer = PROXY_LIST[session_count%len(PROXY_LIST)]
        print(proxyServer)
        if not len(code) == 31:
            print(f"Ignoring invalid code {code}")
            file_io.write_array_to_file(RECEIPT_CODES, code_file_path)
            continue

        print(f"Taking the survey with code {code}...")

        # Set up the browser
        url = "https://mcdvoice.com"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"--proxy-server={proxyServer}")
        if conf.IS_HIDDEN_BROWSER:
            chrome_options.add_argument(f"--headless")
            chrome_options.add_argument(f"--window-size={WINDOW_SIZE}")
        browser = webdriver.Chrome(options=chrome_options)

        # Go to the voice survey site

        browser.get(url)

        # Get all the boxes
        try:
            cn1 = browser.find_element(By.ID, "CN1")
            cn2 = browser.find_element(By.ID, "CN2")
            cn3 = browser.find_element(By.ID, "CN3")
            cn4 = browser.find_element(By.ID, "CN4")
            cn5 = browser.find_element(By.ID, "CN5")
            cn6 = browser.find_element(By.ID, "CN6")
        except Exception as e:
            print(e)
            print("survey failed, deleting code, skipping survey.\n")
            continue
        # testing what is my ip
        # browser.get("https://whatismyipaddress.com")
        # time.sleep(120)



        # Get the code parts
        codeParts = code.split("-")

        # Fill all the boxes with the right code parts
        cn1.send_keys(codeParts[0])
        cn2.send_keys(codeParts[1])
        cn3.send_keys(codeParts[2])
        cn4.send_keys(codeParts[3])
        cn5.send_keys(codeParts[4])
        cn6.send_keys(codeParts[5])

        # Click to the next page
        clickNext(browser, SECONDS_DELAY)

        # Check if for some reason the code wasn't valid
        if "Error: We are unable to continue the survey based on the information you provided." in browser.page_source:
            print(f"Ignoring invalid code {code}")
            browser.close()
            browser.quit()
            continue

        try:
            take_survey(browser, SECONDS_DELAY, session_count)
            print(f"Finished survey with code {code}\n")
            session_count += 1
        except Exception as e:
            print(e)
            print("survey failed, deleting code, skipping survey.\n")

        # Close the browser
        browser.close()
        browser.quit()

        # increase session count and update files
        file_io.write_array_to_file(RECEIPT_CODES, code_file_path)




    print(f"Completed {session_count} survey(s)")
    print("No more codes. Feed me more codes. Yum yum!")
