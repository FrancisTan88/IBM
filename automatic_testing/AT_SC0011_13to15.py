from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import numpy as np
import pandas as pd
from datetime import time as dt

"""
SC_Case 11, 13~15
"""

attribute_id = 'id'
attribute_class = 'class'
attribute_xpath = 'xpath'
attribute_css = 'css'


def toInt(whetherNA, value):
    if whetherNA :
        value = value.astype(int)
        return value
    else:
        return value


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
        print("fail to log in")
        driver.quit()


def CreateCase(CaseType):
    try:
        ################################################################  Address  ################################################################################
        locate_submission = '/html/body/app-root/div[1]/app-layout/div/app-side-menu/p-sidebar[2]/div/div/div/ul/li[1]/a/div'    
        locate_company = '/html/body/app-root/div[1]/app-layout/div/div/div/app-leading-page/div[1]/div[1]/div/p-dropdown/div/span'
        locate_CBMY = '/html/body/app-root/div[1]/app-layout/div/div/div/app-leading-page/div[1]/div[1]/div/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]'
        locate_NewApplication = '/html/body/app-root/div[1]/app-layout/div/div/div/app-leading-page/div[1]/div[2]/p-radiobutton/div'
        locate_ProductName = '/html/body/app-root/div[1]/app-layout/div/div/div/app-leading-page/div[1]/div[3]/div/div/p-dropdown/div/span'
        locate_space = '/html/body/app-root/div[1]/app-layout/div/div/div/app-leading-page/div[1]/div[3]/div/div/p-dropdown/div/div[3]/div[1]/div/input'
        locate_next = '/html/body/app-root/div[1]/app-layout/div/div/div/app-leading-page/div[2]/a'

        ################################################################  Execution: Create New Case  ################################################################################
        element = Press(locate_submission, attribute_xpath)
        time.sleep(1)
        element = Press(locate_company, attribute_xpath)
        time.sleep(1)
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
        time.sleep(4)

    except:
        print("fail to create case")
        driver.quit()


def FillCustomerInformation(ID_No):
    try:
        ################################################################  Address  ################################################################################
        locate_IDNO = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[3]/app-customer-information/div/form/div/div[1]/div[2]/input'
        locate_ResidentialStatus = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[3]/app-customer-information/div/form/div/div[3]/div/p-dropdown/div/span'
        locate_withoutlown = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[3]/app-customer-information/div/form/div/div[3]/div/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li'
        locate_next = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[10]/div[2]/a'
        locate_random = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[3]/app-customer-information/div/form/div/div[3]'

        ################################################################  Execution: Fill it  ################################################################################
        element = Type(locate_IDNO, ID_No, attribute_xpath)
        time.sleep(1)
        element = Press(locate_random, attribute_xpath) 
        time.sleep(5)
        element = Press(locate_ResidentialStatus, attribute_xpath) 
        time.sleep(1)
        element = Press(locate_withoutlown, attribute_xpath)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        element = Press(locate_next, attribute_xpath)
        time.sleep(3)

    except:
        print("fail to fill in customer information")
        driver.quit()


def FillEmployment():
    try:
        ################################################################  Address  ################################################################################
        locate_occupation = '//*[@id="occupation"]/div/div[2]/span'
        locate_FactoryOperator = '//*[@id="occupation"]/div/div[3]/div/ul/p-dropdownitem[1]/li'
        locate_MonthlyIncome = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[4]/app-employment/div/form/div[2]/div[2]/div[2]/p-inputnumber/span/input'
        locate_RegAdd = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[4]/app-employment/div/form/div[4]/div/div/app-address-input/form/div/div[3]/div[1]/div/button[1]/span'
        locate_WorkPhoneNo = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[4]/app-employment/div/form/div[5]/div[1]/input'
        locate_next = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[10]/div[2]/a'

        MonthlyIncome = 88888
        WorkPhoneNo = 123

        ################################################################  Execution: Fill it  ################################################################################
        element = Press(locate_occupation, attribute_xpath)
        time.sleep(1)
        element = Press(locate_FactoryOperator, attribute_xpath)
        time.sleep(1)
        element = Type(locate_MonthlyIncome, MonthlyIncome, attribute_xpath)
        time.sleep(1)
        element = Press(locate_RegAdd, attribute_xpath)
        time.sleep(1)
        element = Type(locate_WorkPhoneNo, WorkPhoneNo, attribute_xpath)
        time.sleep(1)
        element = Press(locate_next, attribute_xpath)
        time.sleep(3)

    except:
        print("fail to fill in employment")
        driver.quit()


def FillGuarantorPerson(PersonalID, CorporateID, CustomerName, MobilePhone):
    try:
        ################################################################  Address  ################################################################################
        locate_AddGuarantorPerson = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[2]/div/button/span[2]'
        locate_AddGuarantorPerson2 = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[2]/button/span[2]'

        locate_PersonalID = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[1]/div[2]/form/div[1]/div[2]/input'
        locate_CorporateID = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[2]/div[2]/form/div[1]/div[2]/input'

        locate_PersonalLegalRelationship = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[1]/div[2]/form/div[1]/div[3]/p-dropdown/div/div[2]/span'
        locate_CorporateLegalRelationship = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[2]/div[2]/form/div[1]/div[3]/p-dropdown/div/div[2]/span'
        locate_PersonalRelationship = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[1]/div[2]/form/div[2]/div[2]/p-dropdown/div/div[2]/span'
        locate_CorporateRelationship = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[2]/div[2]/form/div[2]/div[2]/p-dropdown/div/div[2]/span'

        locate_Brother = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[1]/div[2]/form/div[2]/div[2]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[4]/li'
        locate_Sister = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[2]/div[2]/form/div[2]/div[2]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[5]/li'

        locate_IdentityType = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[2]/div[2]/form/div[1]/div[1]/p-dropdown/div/div[2]/span'
        locate_IdentityCorporation = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[2]/div[2]/form/div[1]/div[1]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[2]/li'

        locate_PersonalGuarantor = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[1]/div[2]/form/div[1]/div[3]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li'
        locate_CorporateGuarantor = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[2]/div[2]/form/div[1]/div[3]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li'

        locate_CustomerName = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[2]/div[2]/form/div[2]/div[1]/input'
        locate_MobilePhone = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[2]/div[2]/form/div[2]/div[3]/input'

        locate_next = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[10]/div[2]/a'

        ################################################################  Execution: Fill it  ################################################################################
        element = Press(locate_AddGuarantorPerson, attribute_xpath) 
        time.sleep(1)
        element = Press(locate_AddGuarantorPerson2, attribute_xpath) 
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        element = Type(locate_PersonalID, PersonalID, attribute_xpath)
        time.sleep(1)
        element = Press(locate_PersonalLegalRelationship, attribute_xpath)  #for the information loading
        time.sleep(3)

        element = Press(locate_IdentityType, attribute_xpath)
        time.sleep(1)
        element = Press(locate_IdentityCorporation, attribute_xpath)
        time.sleep(1)
        element = Type(locate_CorporateID, CorporateID, attribute_xpath)
        time.sleep(1)

        element = Press(locate_PersonalLegalRelationship, attribute_xpath)  
        time.sleep(1)
        element = Press(locate_PersonalGuarantor, attribute_xpath)

        element = Press(locate_PersonalRelationship, attribute_xpath)
        time.sleep(1)
        element = Press(locate_Brother, attribute_xpath)

        element = Press(locate_CorporateLegalRelationship, attribute_xpath)
        time.sleep(1)
        element = Press(locate_CorporateGuarantor, attribute_xpath)

        element = Press(locate_CorporateRelationship, attribute_xpath)
        time.sleep(1)
        element = Press(locate_Sister, attribute_xpath)

        element = Type(locate_CustomerName, CustomerName, attribute_xpath)
        time.sleep(1)
        element = Type(locate_MobilePhone, MobilePhone, attribute_xpath)
        time.sleep(1)

        element = Press(locate_next, attribute_xpath)
        time.sleep(3)
    
    except:
        print("fail to fill in guarantor person")
        driver.quit()


def FillContactPerson():
    try:
        ################################################################  Address  ################################################################################
        locate_AddContactPerson = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[6]/app-contact-person/div/div/button/span[2]'
        locate_AddContactPerson2 = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[6]/app-contact-person/div[2]/button/span[2]'

        locate_Name1 = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[6]/app-contact-person/div[1]/form/div[1]/div[1]/input'
        locate_Name2 = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[6]/app-contact-person/div[2]/form/div[1]/div[1]/input'

        locate_ContactPersonRelationship1 = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[6]/app-contact-person/div[1]/form/div[1]/div[2]/p-dropdown/div/div[2]/span'
        locate_ContactPersonRelationship2 = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[6]/app-contact-person/div[2]/form/div[1]/div[2]/p-dropdown/div/div[2]/span'

        locate_ContactPersonMobilePhone1 = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[6]/app-contact-person/div[1]/form/div[2]/div[2]/input'
        locate_ContactPersonMobilePhone2 = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[6]/app-contact-person/div[2]/form/div[2]/div[2]/input'

        locate_parents = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[6]/app-contact-person/div[1]/form/div[1]/div[2]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li'
        locate_spouse = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[6]/app-contact-person/div[2]/form/div[1]/div[2]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[2]/li'

        locate_next = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[10]/div[2]/a'

        Name1 = 'aa'
        Name2 = 'bb'
        Phone1 = '123'
        Phone2 = '321'

        ################################################################  Execution: Fill it  ################################################################################
        element = Press(locate_AddContactPerson, attribute_xpath)
        time.sleep(1)
        element = Press(locate_AddContactPerson2, attribute_xpath)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        element = Type(locate_Name1, Name1, attribute_xpath)
        
        element = Press(locate_ContactPersonRelationship1, attribute_xpath)
        time.sleep(1)
        element = Press(locate_parents, attribute_xpath)
        time.sleep(1)
        element = Type(locate_ContactPersonMobilePhone1, Phone1, attribute_xpath)
        time.sleep(1)

        element = Type(locate_Name2, Name2, attribute_xpath)
        time.sleep(1)
        element = Press(locate_ContactPersonRelationship2, attribute_xpath)
        time.sleep(1)
        element = Press(locate_spouse, attribute_xpath)
        time.sleep(1)
        element = Type(locate_ContactPersonMobilePhone2, Phone2, attribute_xpath)
        time.sleep(1)

        element = Press(locate_next, attribute_xpath)
        time.sleep(3)

    except:
        print("fail to fill in contact person")
        driver.quit()


def FillCollateral():
    try:
        ################################################################  Address  ################################################################################
        locate_AddCollateral = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion'

        locate_property = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[1]/p-dropdown/div/div[2]'
        locate_FinanceAsset = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[1]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]'

        locate_category = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[2]/p-dropdown/div/div[2]/span'
        locate_CommercialVehicle = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[2]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li'

        locate_HasValue = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[3]/p-dropdown/div/div[2]/span'
        locate_Y = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[3]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li'

        locate_brand = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[4]/p-dropdown/div/div[2]/span'
        locate_Adiva = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[4]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[5]/li'

        locate_model = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[5]/p-dropdown/div/div[2]/span'
        locate_AD3 = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[5]/p-dropdown/div/div[3]/div/ul/p-dropdownitem/li'

        locate_transaction = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[6]/p-dropdown/div/div[2]/span'
        locate_new = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[6]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li'

        locate_date = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[7]/div[2]/p-calendar/span/button/span[1]'
        locate_left = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[7]/div[2]/p-calendar/span/div/div[1]/div/div/button[1]'
        locate_August = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[7]/div[2]/p-calendar/span/div/div[2]/span[8]'

        locate_manu = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[10]/p-dropdown/div/div[2]/span'
        locate_BMW = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[10]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li/span[1]'

        locate_transmission = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[11]/p-dropdown/div/div[2]/span'
        locate_auto = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[11]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[2]/li'

        locate_PurchasePrice = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[15]/div[2]/sigv-currency/div/p-inputnumber/span/input'
        locate_SalesApprisalPrice = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[1]/div[16]/div[2]/sigv-currency/div/p-inputnumber/span/input'

        locate_DownPayment = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[2]/div[1]/div[2]/sigv-currency/div/p-inputnumber/span/input'

        locate_GPSinstallation = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[2]/div[3]/p-dropdown/div/div[2]/span'
        locate_None = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[7]/app-collateral/div[1]/div/p-accordion/div/p-accordiontab/div/div[2]/div/div[1]/div[2]/app-collateral-vehicle-motor/div/form/div/div[2]/div[3]/p-dropdown/div/div[3]/div/ul/p-dropdownitem/li'

        locate_next = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[10]/div[2]/a'

        PurchasePrice = '99999'
        SalesApprisalPrice = PurchasePrice
        DownPayment = '33333'

        ################################################################  Execution: Fill it  ################################################################################
        element = Press(locate_AddCollateral, attribute_xpath)
        time.sleep(5)

        element = Press(locate_property, attribute_xpath)
        time.sleep(1)
        element = Press(locate_FinanceAsset, attribute_xpath)

        element = Press(locate_category, attribute_xpath)
        time.sleep(1)
        element = Press(locate_CommercialVehicle, attribute_xpath)

        element = Press(locate_HasValue, attribute_xpath)
        time.sleep(1)
        element = Press(locate_Y, attribute_xpath)

        element = Press(locate_brand, attribute_xpath)
        time.sleep(1.5)
        element = Press(locate_Adiva, attribute_xpath)
        time.sleep(1)

        element = Press(locate_model, attribute_xpath)
        time.sleep(1)
        element = Press(locate_AD3, attribute_xpath)

        element = Press(locate_transaction, attribute_xpath)
        time.sleep(1)
        element = Press(locate_new, attribute_xpath)

        element = Press(locate_date, attribute_xpath)
        time.sleep(1)
        element = Press(locate_left, attribute_xpath)
        time.sleep(1)
        element = Press(locate_August, attribute_xpath)

        element = Press(locate_manu, attribute_xpath)
        time.sleep(1)
        element = Press(locate_BMW, attribute_xpath)

        element = Press(locate_transmission, attribute_xpath)
        time.sleep(1)
        element = Press(locate_auto, attribute_xpath)

        element = Type(locate_PurchasePrice, PurchasePrice, attribute_xpath)
        time.sleep(1)
        element = Type(locate_SalesApprisalPrice, SalesApprisalPrice, attribute_xpath)
        time.sleep(1)
        element = Type(locate_DownPayment, DownPayment, attribute_xpath)
        time.sleep(1)

        element = Press(locate_GPSinstallation, attribute_xpath)
        time.sleep(1)
        element = Press(locate_None, attribute_xpath)
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        element = Press(locate_next, attribute_xpath)
        time.sleep(3)

    except:
        print("fail to fill in collateral")
        driver.quit()


def FillTermsConditions():
    try:
        ################################################################  Address  ################################################################################
        locate_DealSource = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[8]/app-terms-conditions/div/div[1]/div[2]/div[1]/p-dropdown/div/div[2]/span'
        locate_CarDealer = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[8]/app-terms-conditions/div/div[1]/div[2]/div[1]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li'
        locate_DealerName = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[8]/app-terms-conditions/div/div[1]/div[2]/div[2]/p-dropdown/div/div[2]/span'
        locate_InputName = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[8]/app-terms-conditions/div/div[1]/div[2]/div[2]/p-dropdown/div/div[3]/div[1]/div/input'
        locate_SalesName = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[8]/app-terms-conditions/div/div[1]/div[2]/div[3]/p-dropdown/div/div[2]/span'
        locate_PAIDAIAH = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[8]/app-terms-conditions/div/div[1]/div[2]/div[3]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[2]/li'
        locate_QuotesType = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[8]/app-terms-conditions/div/div[1]/div[3]/div[1]/p-dropdown/div/div[2]/span'
        locate_ETP = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[8]/app-terms-conditions/div/div[1]/div[3]/div[1]/p-dropdown/div/div[3]/div/ul/p-dropdownitem/li'
        locate_InterestRate = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[8]/app-terms-conditions/div/div[1]/div[3]/div[2]/div[2]/p-inputnumber/span/input'
        locate_CommisionDeduction = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[8]/app-terms-conditions/div/div[2]/div/div/p-table/div/div/table/tbody/tr[1]/td[5]/p-checkbox/div/div[2]'
        locate_ApplyTerms = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[8]/app-terms-conditions/div/div[4]/div/div[1]/p-inputnumber/span/input'
        locate_random2 = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[8]/app-terms-conditions/div/div[4]'
        locate_next = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[10]/div[2]/a'

        DealerName = 'JHR0001 Twit'
        InterestRate = 8
        Terms = 50

        ################################################################  Execution: Fill it  ################################################################################
        element = Press(locate_DealSource, attribute_xpath)
        time.sleep(1)
        element = Press(locate_CarDealer, attribute_xpath)

        element = Press(locate_DealerName, attribute_xpath)
        time.sleep(1)
        element = Type(locate_InputName, DealerName, attribute_xpath)
        time.sleep(1)
        element.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        element.send_keys(Keys.ENTER)
        time.sleep(1)

        element = Press(locate_SalesName, attribute_xpath)
        time.sleep(1)
        element = Press(locate_PAIDAIAH, attribute_xpath)
        time.sleep(0.5)

        element = Press(locate_QuotesType, attribute_xpath)
        time.sleep(1)
        element = Press(locate_ETP, attribute_xpath)
        time.sleep(0.5)

        element = Type(locate_InterestRate, InterestRate, attribute_xpath)
        time.sleep(1)

        element = Press(locate_CommisionDeduction, attribute_xpath)
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        element = Type(locate_ApplyTerms, Terms, attribute_xpath)
        time.sleep(1)

        element = Press(locate_random2, attribute_xpath)
        time.sleep(3)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        element = Press(locate_next, attribute_xpath)
        time.sleep(3)

    except:
        print("fail to fill in terms and conditions")
        driver.quit()


def FillAttachment():
    try:
        locate_submit = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/sigv-fixed-bottom-panel/div/div/div/div/div/div[1]/a'

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        element = Press(locate_submit, attribute_xpath)
        time.sleep(10)

    except:
        print("fail to submit the case")
        driver.quit()


def Search(ID_No):
    try:
        locate_SearchSidebar = '/html/body/app-root/div[1]/app-layout/div/app-side-menu/p-sidebar[2]/div/div/div/ul/li[3]/a/div/img'
        locate_SearchIdno = '/html/body/app-root/div[1]/app-layout/div/div/div/app-index/p-accordion/div/p-accordiontab/div/div[2]/div/div/div[1]/div[2]/div/div/input'
        locate_SearchButton = '/html/body/app-root/div[1]/app-layout/div/div/div/app-index/p-accordion/div/p-accordiontab/div/div[2]/div/div/div[6]/div/div/div/div/a[1]'

        element = Press(locate_SearchSidebar, attribute_xpath)
        time.sleep(3)

        element = Type(locate_SearchIdno, ID_No, attribute_xpath)
        time.sleep(1)

        element = Press(locate_SearchButton, attribute_xpath)
        time.sleep(8)
    
    except:
        print("fail to search the case")
        driver.quit()


if __name__ == "__main__":

    s = Service('./chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    url = 'https://sit01-websubmission.chailease.com.my/websubmission-ui/'
    driver.get(url)
    time.sleep(3)

    file_path = '/Users/kian199887/Downloads/github_francistan88/DSA/automatic_testing/submission_information.xlsx'
    data = pd.read_excel(file_path)
    df = pd.DataFrame(data)
    notNA = df['Mobile Phone'].notna()

    # Guarantor Part:
    ID_No = int(df['IdNo'].iloc[0])
    PersonalID = int(df['Guarantor Person(Indi)'].iloc[0])
    CorporateID = df['Guarantor Person(Corpo)'].iloc[0]
    CustomerName = df['Customer Name'].iloc[0] 
    MobilePhone = toInt(notNA[0], df['Mobile Phone'][0])
    MobilePhone = '0'+str(MobilePhone)

    login_email = 'nabiladibidris@chailease.com.my'
    CaseType = 'SC_Case'
    

    LogIn(login_email)    

    CreateCase(CaseType)

    FillCustomerInformation(ID_No)

    FillEmployment()

    FillGuarantorPerson(PersonalID, CorporateID, CustomerName, MobilePhone)

    FillContactPerson()

    FillCollateral()

    FillTermsConditions()

    FillAttachment()

    Search(ID_No)




