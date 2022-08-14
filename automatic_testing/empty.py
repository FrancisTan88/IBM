from queue import Empty
from xml.dom.minidom import Element
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from openpyxl import Workbook, load_workbook
import time
from time import sleep
import numpy as np
import pandas as pd
import pyodbc
import requests
import sys

attribute_id = 'id'
attribute_class = 'class'
attribute_xpath = 'xpath'
attribute_css = 'css'


def LocateByAttribute(attribute, locate_name):
    if attribute == 'id':
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locate_name)))

    elif attribute == 'class':
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, locate_name)))

    elif attribute == 'xpath':
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, locate_name)))
    
    elif attribute == 'css':
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, locate_name)))

    return element


# def LocateByText(locate_name, text_name):
#     text_name = '"' + text_name + '"'
#     element = driver.find_element(By.XPATH, locate_name + f'//*[contains(text(), {text_name})]')   
#     return element


def Press(locate_name, attribute):
    element = LocateByAttribute(attribute, locate_name)
    element.click()
    return element


def Type(locate_name, type_value, attribute):
    element = LocateByAttribute(attribute, locate_name)
    element.send_keys(type_value)
    return element

def LogIn(login_email):
    locate_email = 'userEmail'
    try:
        element = Type(locate_email, login_email, attribute_id)
        time.sleep(1)
        element.send_keys(Keys.ENTER)
        time.sleep(3)

    except:
        # driver.quit()
        sys.exit("fail to log in")

def CreateCase(CaseType):
    try:
        ################################################################  Address  ################################################################################
        text_name = 'CBMY'

        locate_submission = '/html/body/app-root/div[1]/app-layout/div/app-side-menu/p-sidebar[2]/div/div/div/ul/li[1]/a/div'    
        # locate_company = '/html/body/app-root/div[1]/app-layout/div/div/div/app-leading-page/div[1]/div[1]/div/p-dropdown/div/span'
        locate_company = '/html/body/app-root/div[1]/app-layout/div/div/div/app-leading-page/div[1]/div[1]/div/p-dropdown/div/span'
        locate_CBMY = '/html/body/app-root/div[1]/app-layout/div/div/div/app-leading-page/div[1]/div[1]/div/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]'
        locate_NewApplication = '/html/body/app-root/div[1]/app-layout/div/div/div/app-leading-page/div[1]/div[2]/p-radiobutton/div'
        locate_ProductName = '/html/body/app-root/div[1]/app-layout/div/div/div/app-leading-page/div[1]/div[3]/div/div/p-dropdown/div/span'
        locate_space = '/html/body/app-root/div[1]/app-layout/div/div/div/app-leading-page/div[1]/div[3]/div/div/p-dropdown/div/div[3]/div[1]/div/input'
        locate_next = '/html/body/app-root/div[1]/app-layout/div/div/div/app-leading-page/div[2]/a'

        ################################################################  Execution: Create New Case  ################################################################################
        element = Press(locate_submission, attribute_xpath)
        time.sleep(2)
        # element = LocateByText(locate_company, text_name)
        element = Press(locate_company, attribute_xpath)
        # print(element.text)
        time.sleep(1)
        # element.click()
        element = Press(locate_CBMY, attribute_xpath)
        time.sleep(3)
        element = Press(locate_NewApplication, attribute_xpath)   
        time.sleep(1)
        element = Press(locate_ProductName, attribute_xpath)
        time.sleep(1) 
        element = Type(locate_space, CaseType, attribute_xpath)  
        time.sleep(1)
        element.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        element.send_keys(Keys.ENTER)
        time.sleep(1)
        element = Press(locate_next, attribute_xpath)
        time.sleep(5)

    except:
        # driver.quit()
        sys.exit("fail to create case")

def FillCustomerInformation(ID_No):
    try:
        ################################################################  Address  ################################################################################
        locate_IDNO = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[3]/app-customer-information/div/form/div/div[1]/div[2]/input'
        locate_ResidentialStatus = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[3]/app-customer-information/div/form/div/div[3]/div/p-dropdown/div/span'
        locate_withoutlown = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[3]/app-customer-information/div/form/div/div[3]/div/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li'
        locate_next = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[10]/div[2]/a'
        locate_random = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[3]/app-customer-information/div/form/div/div[3]'
        locate_nationality = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[3]/app-customer-information/div/form/div/div[2]/div[4]/p-dropdown/div/div[2]/span'
        locate_citizen = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[3]/app-customer-information/div/form/div/div[2]/div[4]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li'

        ################################################################  Execution: Fill it  ################################################################################
        element = Type(locate_IDNO, ID_No, attribute_xpath)
        time.sleep(1)
        element = Press(locate_random, attribute_xpath) 
        time.sleep(5)
        element = Press(locate_nationality, attribute_xpath)
        sleep(1)
        element = Press(locate_citizen, attribute_xpath)
        sleep(1)
        element = Press(locate_ResidentialStatus, attribute_xpath) 
        time.sleep(1)
        element = Press(locate_withoutlown, attribute_xpath)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        element = Press(locate_next, attribute_xpath)
        time.sleep(3)

    except:
        # driver.quit()
        sys.exit("fail to fill in customer information")

s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
url = 'https://sit01-websubmission.chailease.com.my/websubmission-ui/'
driver.get(url)
time.sleep(3)

login_email = 'nabiladibidris@chailease.com.my'
CaseType = 'SC_Case'


LogIn(login_email)    

CreateCase(CaseType)

locate_IDNO = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[3]/app-customer-information/div/form/div/div[1]/div[2]/input'
locate_IT = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[3]/app-customer-information/div/form/div/div[1]/div[1]/div[2]/div[1]/p-dropdown/div/span'
locate_CN = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[2]/div[2]/form/div[2]/div[1]/input'
locate_random = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[3]/app-customer-information/div/form/div/div[3]'
locate_name = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[3]/app-customer-information/div/form/div/div[2]/div[1]/input'
ID_No = '880520435314'
# element = LocateByAttribute(attribute_xpath, locate_IDNO)
# print(element)

# it = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, locate_IT))).get_attribute("value")
# id_text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, locate_IDNO))).text




element = Type(locate_IDNO, ID_No, attribute_xpath)
time.sleep(1)
element = Press(locate_random, attribute_xpath) 
time.sleep(8)
text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locate_name))).get_attribute("value")
print(type(text))
print(text)


# if not text:
#     print("empty str")
# if text == "":
#     print("empty str again")