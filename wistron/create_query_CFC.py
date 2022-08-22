from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from time import sleep
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


def Type(locate_name, type_value, attribute):
    element = LocateByAttribute(attribute, locate_name)
    element.send_keys(type_value)
    return element


def Press(locate_name, attribute):
    element = LocateByAttribute(attribute, locate_name)
    element.click()
    return element


def GetElementText(locate_name):
    text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locate_name))).get_attribute("value")
    return text


def FillCreate(id, pmt):
    locate_id = '/html/body/input[1]'
    locate_pmt = '/html/body/input[2]'
    locate_confirm = '/html/body/button[1]'
    locate_popup_id = '/html/body/label[3]'
    # locate_popup_id = 'result'
    locate_redirect = '/html/body/button[2]'

    try:
        element = Type(locate_id, id, attribute_xpath)
        time.sleep(1)

        element = Type(locate_pmt, pmt, attribute_xpath)
        time.sleep(1)

        element = Press(locate_confirm, attribute_xpath)
        time.sleep(1)
        
        # element = LocateByAttribute(attribute_id, locate_popup_id)
        # txt = element.getText()
        element_idTxt = LocateByAttribute(attribute_xpath, locate_popup_id)
        id_txt = element_idTxt.text
        time.sleep(1)
        
        if not id_txt:
            sys.exit("fail to get text")

        element = Press(locate_redirect, attribute_xpath)
        time.sleep(1)
        
        return id_txt
        
    except:
        sys.exit("fail to create")


def FillQuery(id):
    locate_orderid = '/html/body/input'
    locate_confirm = '/html/body/button'
    
    try:
        element = Type(locate_orderid, id, attribute_xpath)
        time.sleep(1)

        element = Press(locate_confirm, attribute_xpath)
        time.sleep(1)

    except:
        sys.exit("fail to query")



if __name__ == "__main__":

    # open the submission web 
    s = Service('./chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')  # to avoid: certificate problems caused by 3rd browser

    driver = webdriver.Chrome(service=s, chrome_options=options)
    driver.maximize_window()
    url_create = 'file:///Users/kian199887/Downloads/github_francistan88/DSA/wistron/Create.html'
    driver.get(url_create)
    time.sleep(3)

    # value of Create:
    user_id = 'aaaa'
    payment_type = 0
    
    id_text = FillCreate(user_id, payment_type)
    
    FillQuery(id_text)



    