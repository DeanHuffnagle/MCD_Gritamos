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


def getChoice(customChoices: list = ["Opt5", "Opt4", "Opt3", "Opt2", "Opt1"], customWeights=(100, 0, 0, 0, 0)):
    return random.choices(customChoices, weights=customWeights, k=1)[0]


def clickNext(browser, delay):
    time.sleep(delay)
    browser.get_screenshot_as_file("Screenshots/currentPage.png")
    browser.find_element(By.ID, "NextButton").click()


def solveTablesWithRadioButtons(browser):
    table = browser.find_element(By.TAG_NAME, "table")
    trs = table.find_elements(By.CSS_SELECTOR, ".InputRowOdd, .InputRowEven")
    for tr in trs:
        opt = getChoice()
        tr.find_element(By.CLASS_NAME, opt).find_element(By.CLASS_NAME, "radioSimpleInput").click()


def leaveComment(browser, count):
    commentBox = browser.find_element(By.TAG_NAME, "textarea")
    feedback = generate_response(count)
    commentBox.send_keys(feedback)
    return True


def solveSingleRadioOption(browser):
    optionLists = browser.find_element(By.CLASS_NAME, "rbListContainer").find_elements(By.CLASS_NAME, "rbList")
    choice = random.choice(optionLists)
    choice.find_element(By.CLASS_NAME, "radioSimpleInput").click()

def take_survey(browser, delay, num):
    is_drive_thru = True
    # Page 1, how did you order?
    print("page 1")
    browser.find_element(By.CLASS_NAME, "Opt1").find_element(By.CLASS_NAME, "radioSimpleInput").click()
    clickNext(browser, delay)

    # page 2 Drive-Thru, Carry-Out, Mobile, etc.
    print("page 2")
    try:
        browser.find_element(By.CLASS_NAME, "Opt2").find_element(By.CLASS_NAME, "radioSimpleInput").click()
    except:
        is_drive_thru = False
        browser.find_element(By.CLASS_NAME, "Opt3").find_element(By.CLASS_NAME, "radioSimpleInput").click()
    clickNext(browser, delay)

    # page 3, highly satisfied
    print("page 3")
    browser.find_element(By.CLASS_NAME, "Opt5").find_element(By.CLASS_NAME, "radioSimpleInput").click()
    clickNext(browser, delay)

    # page 4, are you a rewards member?
    print("page 4")
    browser.find_element(By.CLASS_NAME, "Opt2").find_element(By.CLASS_NAME, "radioSimpleInput").click()
    clickNext(browser, delay)

    # page 5, did the employee ask if you are using the mobile app?
    print("page 5")
    browser.find_element(By.CLASS_NAME, "Opt1").find_element(By.CLASS_NAME, "radioSimpleInput").click()
    clickNext(browser, delay)

    # page 6, rate satistfaction
    print("page 6")
    solveTablesWithRadioButtons(browser)
    clickNext(browser, delay)

    # page 7, rate satisfaction part 2
    solveTablesWithRadioButtons(browser)
    print("page 7")
    clickNext(browser, delay)

    # page 8, what did you order (optional. skip.)
    print("page 8")
    clickNext(browser, delay)

    # page 9, did you have a problem? no.
    print("page 9")
    browser.find_element(By.CLASS_NAME, "Opt2").find_element(By.CLASS_NAME, "radioSimpleInput").click()
    clickNext(browser, delay)

    # page 10, return soon?
    print("page 10")
    solveTablesWithRadioButtons(browser)
    clickNext(browser, delay)

    # page 11, leave a comment
    print("page 11")
    leaveComment(browser, num)
    # time.sleep(20)
    clickNext(browser, delay)

    # page 12, were you asked to pull forward?
    if is_drive_thru:
        print("page 12 (drive thru only)")
        browser.find_element(By.CLASS_NAME, "Opt2").find_element(By.CLASS_NAME, "radioSimpleInput").click()
        clickNext(browser, delay)

    # page 13,  how many times have you been here?
    print("page 13")
    browser.find_element(By.CLASS_NAME, "Opt4").find_element(By.CLASS_NAME, "radioSimpleInput").click()
    clickNext(browser, delay)

    # page 14,  favorite food place?
    print("page 14")
    browser.find_element(By.CLASS_NAME, "Opt4").find_element(By.CLASS_NAME, "radioSimpleInput").click()
    clickNext(browser, delay)

    # page 15,  do you trust McDonalds? with your life?
    print("page 15")
    browser.find_element(By.CLASS_NAME, "Opt5").find_element(By.CLASS_NAME, "radioSimpleInput").click()
    clickNext(browser, delay)

    # if it asks for demographic information
    try:
        clickNext(browser, delay)
    except:
        print("didn't ask for demographic information. survey complete.")
    browser.get_screenshot_as_file("Screenshots/capture.png")
