from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import numpy as np
import pandas as pd
import pyodbc
import requests
import sys
import json

attribute_xpath = 'xpath'

def LocateByAttribute(attribute, locate_name):
    if attribute == 'id':
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locate_name)))

    elif attribute == 'class':
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, locate_name)))

    elif attribute == 'xpath':
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locate_name)))
    
    elif attribute == 'css':
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, locate_name)))

    return element


def Type(locate_name, type_value, attribute):
    element = LocateByAttribute(attribute, locate_name)
    element.send_keys(type_value)
    return element


def Press(locate_name, attribute):
    element = LocateByAttribute(attribute, locate_name)
    element.click()
    return element


def GetApplicantEmail(url):
    response = requests.get(url)
    json_data = response.json()
    # email = GetEmailFromJson(json_data)
    # return email


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
url = 'https://sit01-creditratingscales.chailease.com.my/creditratingscales-ui/'
driver.get(url)
sleep(3)

email = 'NurulAmirah@chailease.com.my'
locate_e = '//*[@id="userEmail"]'
locate_login = '/html/body/app-root/div[1]/sigv-login/div[1]/form/div[2]/button'
element = Type(locate_e, email, attribute_xpath)
sleep(1)
element = Press(locate_login, attribute_xpath)
sleep(3)
# response = requests.get(url)
# print(response.status_code)
# data = response.json()
# jprint(data)

/html/body/app-root/div[1]/sigv-layout/div/div/div/app-todo/p-tabview/div/div/p-tabpanel[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div/a/div/div[2]
locate_PCC = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-todo/p-tabview/div/div/p-tabpanel[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div/a[2]/div/div[2]'
element = LocateByAttribute(attribute_xpath, locate_PCC)
sleep(1)
print(element.text)

