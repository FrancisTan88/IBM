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
    
    if not element:
        sys.exit(f"Can not find {locate_name}")

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
    
    if not text:
        sys.exit(f"Can not get the text of {locate_name}")

    return text


def Create(id, pmt):
    locate_id = '/html/body/input[1]'
    locate_pmt = '/html/body/input[2]'
    locate_confirm = '/html/body/button[1]'
    locate_popup_id = '/html/body/label[4]'
    locate_redirect = '/html/body/button[2]'

    try:
        element = Type(locate_id, id, attribute_xpath)
        time.sleep(1)

        element = Type(locate_pmt, pmt, attribute_xpath)
        time.sleep(1)

        element = Press(locate_confirm, attribute_xpath)
        time.sleep(1)
        
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


def Query(userId):
    # locate_redirect = '/html/body/button[2]'
    locate_userId = '/html/body/input'
    locate_confirm = '/html/body/button'
    locate_redirect = '/html/body/button[2]'
    
    try:
        element = Type(locate_userId, userId, attribute_xpath)
        time.sleep(1)

        element = Press(locate_confirm, attribute_xpath)
        time.sleep(1)

        element = Press(locate_redirect, attribute_xpath)
        time.sleep(2)

    except:
        sys.exit("fail to query")


def Update(userId, orderId, itemId, itemName, unitPrice, qty, itemId2, itemName2, unitPrice2, qty2, newId, newItemName, newUnitPrice, newQty, mod_val1, mod_val2):
    locate_userId = '/html/body/input'
    locate_orderId = '/html/body/input[2]'
    locate_query = '/html/body/button[1]'

    locate_newOrderId = '/html/body/div[1]/label[2]'
    locate_newUserId = '/html/body/div[1]/label[4]'
    locate_totalPrice = '/html/body/div[1]/label[6]'

    locate_addNewRow = '/html/body/div[2]/button[1]'
    locate_itemId = '/html/body/div[2]/div/table/tbody/tr/td[2]/input'
    locate_itemName = '/html/body/div[2]/div/table/tbody/tr/td[3]/input'
    locate_unitPrice = '/html/body/div[2]/div/table/tbody/tr/td[4]/input'
    locate_newUnitPrice = '/html/body/div[2]/div/table/tbody/tr[1]/td[4]/input'
    locate_qty = '/html/body/div[2]/div/table/tbody/tr/td[5]/input'
    locate_newQty = '/html/body/div[2]/div/table/tbody/tr[1]/td[5]/input'

    locate_itemId2 = '/html/body/div[2]/div/table/tbody/tr[2]/td[2]/input'
    locate_itemName2 = '/html/body/div[2]/div/table/tbody/tr[2]/td[3]/input'
    locate_unitPrice2 = '/html/body/div[2]/div/table/tbody/tr[2]/td[4]/input'
    locate_qty2 = '/html/body/div[2]/div/table/tbody/tr[2]/td[5]/input'

    locate_remove = '/html/body/div[2]/div/table/tbody/tr[1]/td[6]/button'

    locate_update = '/html/body/div[2]/button[2]'

    action = ActionChains(driver)


    try:
        # input and query
        element = Type(locate_userId, userId, attribute_xpath)
        sleep(1)
        element = Type(locate_orderId, orderId, attribute_xpath)
        sleep(1)
        element = Press(locate_query, attribute_xpath)
        sleep(1)

        # get the texts of OrderId, TotalPrice
        element_orderId = LocateByAttribute(attribute_xpath, locate_newOrderId)
        element_newUserId = LocateByAttribute(attribute_xpath, locate_newUserId)
        element_totalPrice = LocateByAttribute(attribute_xpath, locate_totalPrice)
        txt_newOrderId = element_orderId.text
        txt_newUserId = element_newUserId.text
        txt_totalPrice = element_totalPrice.text
        sleep(1)

        if not txt_newOrderId or not txt_newUserId or not txt_totalPrice:
            sys.exit("fail to get the texts")
        
        # add two rows
        element_addNewRow = Press(locate_addNewRow, attribute_xpath)
        sleep(1)
        element_addNewRow = Press(locate_addNewRow, attribute_xpath)
        sleep(1)
        
        # fill the data
        element = Type(locate_itemId, itemId, attribute_xpath)
        sleep(0.5)
        element = Type(locate_itemName, itemName, attribute_xpath)
        sleep(0.5)
        element_firstRowUnitPrice = Type(locate_unitPrice, unitPrice, attribute_xpath)
        sleep(0.5)
        element_firstRowQty = Type(locate_qty, qty, attribute_xpath)
        sleep(0.5)

        element = Type(locate_itemId2, itemId2, attribute_xpath)
        sleep(0.5)
        element = Type(locate_itemName2, itemName2, attribute_xpath)
        sleep(0.5)
        element = Type(locate_unitPrice2, unitPrice2, attribute_xpath)
        sleep(0.5)
        element = Type(locate_qty2, qty2, attribute_xpath)
        sleep(0.5)
        
        # remove first row
        element = Press(locate_remove, attribute_xpath)
        sleep(0.5)
        
        # add new row and fill it 
        element_addNewRow = Press(locate_addNewRow, attribute_xpath)
        sleep(0.5)
        element = Type(locate_itemId2, newId, attribute_xpath)
        sleep(0.5)
        element = Type(locate_itemName2, newItemName, attribute_xpath)
        sleep(0.5)
        element = Type(locate_unitPrice2, newUnitPrice, attribute_xpath)
        sleep(0.5)
        element = Type(locate_qty2, newQty, attribute_xpath)
        sleep(0.5)

        # modify the unitPrice and Qty in the first row
        element = Press(locate_newUnitPrice, attribute_xpath)
        action.double_click(element).perform()
        element = Type(locate_newUnitPrice, mod_val1, attribute_xpath)
        sleep(0.5)

        element = Press(locate_newQty, attribute_xpath)
        action.double_click(element).perform()
        element = Type(locate_newQty, mod_val2, attribute_xpath)
        sleep(0.5)

        # update it
        element = Press(locate_update, attribute_xpath)

        # detect the alert 
        WebDriverWait(driver, 3).until(EC.alert_is_present(), 'Success')
        sleep(1)
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
        sleep(2)
        

    except:
        sys.exit("fail to update")


def Delete(orderId):
    locate_orderId = '/html/body/input'
    locate_delete = '/html/body/button'

    try:
        element = Type(locate_orderId, orderId, attribute_xpath)
        sleep(1)
        element = Press(locate_delete, attribute_xpath)
        sleep(1)

        # detect the alert 
        WebDriverWait(driver, 3).until(EC.alert_is_present(), 'Success')
        sleep(1)
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
        print("testing is finished, congrats!")

    except:
        sys.exit("fail to delete")



if __name__ == "__main__":

    # open the submission web 
    s = Service('./chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')  # to avoid: certificate problems caused by 3rd browser

    driver = webdriver.Chrome(service=s, chrome_options=options)
    driver.maximize_window()
    url_create = 'file:///Users/kian199887/Downloads/github_francistan88/DSA/wistron/Create.html'
    url_query = 'file:///Users/kian199887/Downloads/github_francistan88/DSA/wistron/Query.html'
    url_update = 'file:///Users/kian199887/Downloads/github_francistan88/DSA/wistron/Update.html'
    url_delete = 'file:///Users/kian199887/Downloads/github_francistan88/DSA/wistron/Delete.html'
    driver.get(url_create)
    time.sleep(3)

    # fill the create:
    user_id = 'aaaa'
    payment_type = 0
    orderId = Create(user_id, payment_type)
    # print(id_text)
    
    # fill the query
    Query(orderId)

    # fill the update
    itemId = "aa"
    itemName = "bb"
    unitPrice = 1
    qty = 2

    itemId2 = "cc"
    itemName2 = "dd"
    unitPrice2 = 3
    qty2 = 4
    
    newId = "ee"
    newItemName = "ff"
    newUnitPrice = 5
    newQty = 6

    mod_val1 = 7
    mod_val2 = 8

    Update(user_id, orderId, itemId, itemName, unitPrice, qty, itemId2, itemName2, unitPrice2, qty2, newId, newItemName, newUnitPrice, newQty, mod_val1, mod_val2)

    # fill the delete
    driver.get(url_delete)
    sleep(2)
    Delete(orderId)
    
    


    