from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.
import time
import numpy as np
import pandas as pd
from datetime import time as dt


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


def LogIn():
    locate_email = 'userEmail'
    login_email = 'MichaelLin@chailease.com.my.bak'
    try:
        element = Type(locate_email, login_email, 'id')
        element.send_keys(Keys.ENTER)
    except:
        print("fail to log in")
        driver.quit()


def Press(locate_name, attribute):
    element = LocateByAttribute(attribute, locate_name)
    element.click()
    return element


if __name__ == "__main__":

    s = Service('./chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    url = 'https://sit01-creditratingscales.chailease.com.my/creditratingscales-ui/92/credit-operations/approval-authority;submissionId=694147'
    driver.get(url)
    LogIn()
    time.sleep(2)
    
    locate_home = '/html/body/app-root/div[1]/sigv-layout/div/div/div/sigv-page-not-found/div/button/span'
    element = Press(locate_home, 'xpath')
    time.sleep(2)

    locate_approval = '//*[@id="p-accordiontab-0-content"]/div/div/a[3]/div/div[1]'
    element = Press(locate_approval, 'xpath')
    time.sleep(3)
    
    locate_738 = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-todo-list/sigv-data-table/div/p-table/div/div[2]/div/div[2]/table/tbody/tr[6]/td[1]/a'
    element = Press(locate_738, 'xpath')
    time.sleep(10)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    locate_submit = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/sigv-fixed-bottom-panel/div/div/div/div/sigv-bpm-btn/div/button[1]/span'
    element = Press(locate_submit, 'xpath')
    time.sleep(3)

    x = driver.switch_to().alert().getText()
    print(x)
    # WebDriverWait(driver, 3).until(EC.alert_is_present())
    # obj = driver.switch_to.alert
    # msg=obj.text
    # print(msg)
    # /html/body/div/div/div[1]/div[1]