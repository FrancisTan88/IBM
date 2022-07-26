from pydoc import locate
from xml.dom.minidom import Element
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time
from time import sleep
import numpy as np
import pandas as pd
import pyodbc
import requests
import sys


"""
SC_Case 11, 13~15
"""

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
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locate_name)))
    
    elif attribute == 'css':
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, locate_name)))

    return element


def LocateByText(locate_name, text_name):
    text_name = '"' + text_name + '"'
    element = driver.find_element(By.XPATH, locate_name + f'/*[contains(text(), {text_name})]')   # select all element that contains text "Preliminary"
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
        driver.quit()
        sys.exit("fail to log in")


def Credit_LogIn(OfficerEmail):
    try:
        locate_e = '//*[@id="userEmail"]'
        credit_login = '/html/body/app-root/div[1]/sigv-login/div[1]/form/div[2]/button'
        element = Type(locate_e, OfficerEmail, attribute_xpath)
        sleep(1)
        element = Press(credit_login, attribute_xpath)
        sleep(6)
    
    except:
        driver.quit()
        sys.exit("fail to log in credit review")


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
        driver.quit()
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
        driver.quit()
        sys.exit("fail to fill in customer information")


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
        # element = Press(locate_occupation, attribute_xpath)
        # time.sleep(1)
        # element = Press(locate_FactoryOperator, attribute_xpath)
        # time.sleep(1)
        # element = Type(locate_MonthlyIncome, MonthlyIncome, attribute_xpath)
        # time.sleep(1)
        # element = Press(locate_RegAdd, attribute_xpath)
        # time.sleep(1)
        # element = Type(locate_WorkPhoneNo, WorkPhoneNo, attribute_xpath)
        # time.sleep(1)
        element = Press(locate_next, attribute_xpath)
        time.sleep(3)

    except:
        driver.quit()
        sys.exit("fail to fill in employment")


def FillGuarantorPerson(PersonalID, CorporateID, CustomerName, MobilePhone):
    try:
        ################################################################  Address  ################################################################################
        locate_AddGuarantorPerson = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[2]/div/button/span[2]'
        locate_AddGuarantorPerson2 = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[2]/button/span[2]'

        locate_PersonalID = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[1]/div[2]/form/div[1]/div[2]/input'
        locate_CorporateID = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[2]/div[2]/form/div[1]/div[2]/input'
            
        locate_PersonalLegalRelationship = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[1]/div[2]/form/div[1]/div[3]/p-dropdown/div/div[2]'
        locate_CorporateLegalRelationship = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[2]/div[2]/form/div[1]/div[3]/p-dropdown/div/div[2]/span'
        locate_PersonalRelationship = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[1]/div[2]/form/div[2]/div[2]/p-dropdown/div/div[2]/span'
        locate_CorporateRelationship = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[2]/div[2]/form/div[2]/div[2]/p-dropdown/div/div[2]/span'

        locate_PersonalRace = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[1]/div[2]/form/div[3]/div[1]/p-dropdown/div/div[2]/span'
        locate_PersonalMalay = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/div[2]/div/div[5]/app-guarantor-person/div[1]/div[1]/div[2]/form/div[3]/div[1]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li'

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
        element.click()
        time.sleep(1)
        element = Press(locate_PersonalGuarantor, attribute_xpath)
        # time.sleep(1)
        element = Press(locate_PersonalRelationship, attribute_xpath)
        time.sleep(1)
        element = Press(locate_Brother, attribute_xpath)
        # time.sleep(1)
        element = Press(locate_PersonalRace, attribute_xpath)
        time.sleep(1)
        element = Press(locate_PersonalMalay, attribute_xpath)
        

        element = Press(locate_IdentityType, attribute_xpath)
        time.sleep(1)
        element = Press(locate_IdentityCorporation, attribute_xpath)
        time.sleep(0.5)
        element = Type(locate_CorporateID, CorporateID, attribute_xpath)
        time.sleep(0.5)

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
        driver.quit()
        sys.exit("fail to fill in guarantor person")


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
        driver.quit()
        sys.exit("fail to fill in contact person")
       


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
        time.sleep(10)

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
        time.sleep(3)   

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
        driver.quit()
        sys.exit("fail to fill in collateral")
        


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
        driver.quit()
        sys.exit("fail to fill in terms and conditions")
        

def FillAttachment():
    try:
        locate_submit = '/html/body/app-root/div[1]/app-layout/div/div/div/app-process/sigv-fixed-bottom-panel/div/div/div/div/div/div[1]/a'

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        element = Press(locate_submit, attribute_xpath)
        time.sleep(15)

    except:
        driver.quit()
        sys.exit("fail to submit the case")
        

# def Search(ID_No):
#     try:
#         locate_SearchSidebar = '/html/body/app-root/div[1]/app-layout/div/app-side-menu/p-sidebar[2]/div/div/div/ul/li[3]/a/div/img'
#         locate_SearchIdno = '/html/body/app-root/div[1]/app-layout/div/div/div/app-index/p-accordion/div/p-accordiontab/div/div[2]/div/div/div[1]/div[2]/div/div/input'
#         locate_SearchButton = '/html/body/app-root/div[1]/app-layout/div/div/div/app-index/p-accordion/div/p-accordiontab/div/div[2]/div/div/div[6]/div/div/div/div/a[1]'

#         element = Press(locate_SearchSidebar, attribute_xpath)
#         time.sleep(3)

#         element = Type(locate_SearchIdno, ID_No, attribute_xpath)
#         time.sleep(1)

#         element = Press(locate_SearchButton, attribute_xpath)
#         time.sleep(10)
    
#     except:
#         driver.quit()
#         sys.exit("fail to search the case")


def GetEmailFromJson(obj):
    return obj['email']


def GetSqlData(cursor, index, by):
    if by == 'IdNo':
        SQL_data = cursor.execute(f"""select CaseNo, CreateTime, CurrentApplicantId, StatusID, StageId, ApplyDate, IdNo, ProductCode from CreditRatingScales.Submission
                        where IdNo = '{index}' 
                        ORDER BY CreateTime DESC
                        """).fetchone()
    elif by == 'CaseNo':
        SQL_data = cursor.execute(f"""select CaseNo, CreateTime, CurrentApplicantId, StatusID, StageId, ApplyDate, IdNo, ProductCode from CreditRatingScales.Submission
                        where CaseNo = '{index}' 
                        ORDER BY CreateTime DESC
                        """).fetchone()

    CaseNo = SQL_data[0]
    CurrentApplicantId = SQL_data[2]
    return CaseNo, CurrentApplicantId


def GetApplicantEmail(url):
    response = requests.get(url)
    json_data = response.json()
    email = GetEmailFromJson(json_data)
    sleep(1)
    return email


def EnterIntoPCR(text_name):
    try:
        locate_main = '//*[@id="p-accordiontab-0-content"]/div'
        element = LocateByText(locate_main, text_name)
        print(element.text)
        sleep(1)
        element.click()
        sleep(10)
    
    except:
        # driver.quit()
        # sys.exit("fail to enter the Premilinary Credit Review")
        print("PCR")


def EnterIntoSM(text_name):
    try:
        locate_main = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-todo/p-tabview/div/div/p-tabpanel[1]/div/p-accordion/div/p-accordiontab/div/div[2]'
        element = LocateByText(locate_main, text_name)
        sleep(1)
        element.click()
        sleep(10)

    except:
        driver.quit()
        sys.exit("fail to enter the Sales Manager Review")


def DataPreprocessing(df, id_isnull):
    for i in range(len(df['IdNo'])):
        if id_isnull[i] == False:
            df['IdNo'].iloc[i] = str(df['IdNo'].iloc[i]).replace('.0', '')
            df['Guarantor Person(Indi)'].iloc[i] = str(df['Guarantor Person(Indi)'].iloc[i]).replace('.0', '')
            df['Guarantor Person(Corpo)'].iloc[i] = str(df['Guarantor Person(Corpo)'].iloc[i]).replace(',', '')
            df['Mobile Phone'].iloc[i] = str(df['Mobile Phone'].iloc[i]).replace('.0', '')
            df['Mobile Phone'].iloc[i] = '0' + str(df['Mobile Phone'].iloc[i])

    return df


def AddCaseToDF(df, row_data, dic_column, CaseNo):
    dic = {}
    date = datetime.today().strftime('%Y-%m-%d')
    status = 1

    for i in range(len(dic_column)):
        dic[dic_column[str(i)]] = row_data[i]

    df = df.append(dic, ignore_index=True)
    df['CaseNo'].iloc[len(df)-1] = CaseNo
    df['Date'].iloc[len(df)-1] = date
    df['Status'].iloc[len(df)-1] = status
    return df


def EnterCase(text_name):
    try:
        locate_body = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-todo-list/sigv-data-table/div/p-table/div/div[2]/div/div[2]'
        element = LocateByText(locate_body, text_name)
        sleep(0.5)
        element.click()
        sleep(12)
    
    except:
        # driver.quit()
        # sys.exit("fail to enter the case")
        print("AAA")


def CreditInstructions():
    try:
        locate_CreditInstructions = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/ul/li[2]/a/span[1]'
        locate_CreditComment = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[2]/div/app-credit-instructions/div/div[1]/div/div/p-dropdown/div/div[2]/span'
        locate_RecommendAppro = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[2]/div/app-credit-instructions/div/div[1]/div/div/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li'
        locate_InstructionsBlock = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[2]/div/app-credit-instructions/div/div[2]/app-instruction/div/div/div[2]/div/textarea'
        locate_decision = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[2]/div/app-credit-instructions/div/div[2]/app-instruction/div/div/div[2]/div/div'
        locate_random = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[2]/div/app-credit-instructions/div/div[1]'
        locate_CustomerInformation = '//*[@id="version-comparison_customer-information"]'
        text_name = 'Approval'
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        element = Press(locate_CreditInstructions, attribute_xpath)
        sleep(1)
        element = Press(locate_CreditComment, attribute_xpath)
        sleep(1)
        element = Press(locate_RecommendAppro, attribute_xpath)
        sleep(0.5)
        element = Press(locate_InstructionsBlock, attribute_xpath)
        sleep(1)
        element = LocateByText(locate_decision, text_name)
        sleep(0.5)
        element.click()
        element = Press(locate_random, attribute_xpath)
        sleep(0.5)
        element = Press(locate_CustomerInformation, attribute_xpath)
        sleep(5)
        
    except:
        driver.quit()
        sys.exit("fail to fill in the Credit Instructions")


def SM_CreditInstructions():
    try:
        locate_CreditInstructions = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/ul/li[2]/a/span[1]'
        locate_CreditComment = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[2]/div/app-credit-instructions/div/div[1]/div/div/p-dropdown/div/div[2]/span'
        locate_RecommendAppro = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[2]/div/app-credit-instructions/div/div[1]/div/div/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li'
        locate_InstructionsBlock = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[2]/div/app-credit-instructions/div/div[2]/app-instruction/div/div/div[2]/div/textarea'
        locate_decision = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[2]/div/app-credit-instructions/div/div[2]/app-instruction/div/div/div[2]/div/div'
        locate_random = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[2]/div/app-credit-instructions/div/div[1]'
        # locate_submit = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/sigv-fixed-bottom-panel/div/div/div/div/sigv-bpm-btn/div/button[1]/span'

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)

        element = Press(locate_CreditInstructions, attribute_xpath)
        sleep(1)
        element = Press(locate_CreditComment, attribute_xpath)
        sleep(1)
        element = Press(locate_RecommendAppro, attribute_xpath)
        sleep(0.5)
        element = Press(locate_InstructionsBlock, attribute_xpath)
        sleep(1)
        element = LocateByText(locate_decision, text_name)
        sleep(0.5)
        element.click()
        element = Press(locate_random, attribute_xpath)
        sleep(0.5)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)

        # element = Press(locate_submit, attribute_xpath)
        # sleep(10)

    except:
        driver.quit()
        sys.exit("fail to fill in the Sales Manager Credit Instructions")

    

def CreditCustomerInformation():
    try:
        locate_EducationLvl = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[3]/div/app-credit-operations-information/div[2]/app-information-individual/div[1]/div[4]/div[1]/div/div/p-dropdown/div/div[2]/span'
        locate_master = '/html/body/div/div/ul/p-dropdownitem[1]/li/span[1]'
        locate_LengthOfResidence = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[3]/div/app-credit-operations-information/div[2]/app-information-individual/div[1]/div[4]/div[3]/div/div/p-inputnumber/span/input'
        locate_collateral = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/ul/li[6]/a/span[1]'
        locate_MobilePhone2 = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[3]/div/app-credit-operations-information/div[2]/app-information-individual/div[2]/div[1]/div[2]/div/app-phone/div[2]/input' 
        LengthOfResidence = 1
        action = ActionChains(driver)

        element = LocateByAttribute(attribute_xpath, locate_MobilePhone2)
        sleep(0.5)
        action.move_to_element(element).perform()
        sleep(1)
        element = Press(locate_EducationLvl, attribute_xpath)
        sleep(1)
        element = Press(locate_master, attribute_xpath)
        sleep(0.5)
        element = Type(locate_LengthOfResidence, LengthOfResidence, attribute_xpath)
        sleep(1)
        element = Press(locate_collateral, attribute_xpath)
        sleep(5)

    except:
        driver.quit()
        sys.exit("fail to fill in the Credit Customer Information")


def CreditCollateral():
    locate_CollateralType = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[6]/div/app-credit-operations-security-asset/div/div/div/div/div/div/div/p-dropdown/div/div[2]/span'
    locate_vehicle = '/html/body/div/div/ul/p-dropdownitem[1]/li/span[1]'
    locate_purpose = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[6]/div/app-credit-operations-security-asset/p-card/div/div[2]/div/app-vehicle-motor/div/div[1]/div[4]/div/p-dropdown/div/div[2]/span'
    locate_selfuse = '/html/body/div/div/ul/p-dropdownitem[1]/li'
    locate_VehicleType = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[6]/div/app-credit-operations-security-asset/p-card/div/div[2]/div/app-vehicle-motor/div/div[2]/div[3]/div/p-dropdown/div/div[2]/span'
    locate_van = '/html/body/div/div/ul/p-dropdownitem[2]/li/span[1]'
    locate_displacement = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[6]/div/app-credit-operations-security-asset/p-card/div/div[2]/div/app-vehicle-motor/div/div[4]/div[2]/div/input'
    locate_FuelType = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[6]/div/app-credit-operations-security-asset/p-card/div/div[2]/div/app-vehicle-motor/div/div[4]/div[4]/div/p-dropdown/div/div[2]/span'
    locate_diesel = '/html/body/div/div/ul/p-dropdownitem[1]/li/span[1]'

    locate_OfficerAppraisalPrice = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[6]/div/app-credit-operations-security-asset/p-card/div/div[2]/div/app-vehicle-motor/div/div[7]/div[3]/div/div[2]/sigv-currency/div/p-inputnumber/span/input'
    locate_AppraisalMethod = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[6]/div/app-credit-operations-security-asset/p-card/div/div[2]/div/app-vehicle-motor/div/div[7]/div[4]/div/p-dropdown/div/div[2]/span'
    locate_internet = '/html/body/div/div/ul/p-dropdownitem[1]/li/span[1]'
    locate_RegistrationType = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[6]/div/app-credit-operations-security-asset/p-card/div/div[2]/div/app-vehicle-motor/div/div[9]/div[4]/div/p-dropdown/div/div[2]/span'
    locate_TitleTransfer = '/html/body/div/div/ul/p-dropdownitem[1]/li/span[1]'

    locate_CreditReport = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/ul/li[8]/a/span[1]'

    displacement = 1
    OfficerAppraisalPrice = 99999
    action = ActionChains(driver)

    element = Press(locate_CollateralType, attribute_xpath)
    sleep(1)
    element = Press(locate_vehicle, attribute_xpath)

    element = Press(locate_purpose, attribute_xpath)
    sleep(1)
    element = Press(locate_selfuse, attribute_xpath)

    element = Press(locate_VehicleType, attribute_xpath)
    sleep(1)
    element = Press(locate_van, attribute_xpath)

    element = Type(locate_displacement, displacement, attribute_xpath)
    sleep(1)

    element = Press(locate_FuelType, attribute_xpath)
    sleep(1)
    element = Press(locate_diesel, attribute_xpath)
    sleep(0.5)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)

    Type(locate_OfficerAppraisalPrice, OfficerAppraisalPrice, attribute_xpath)
    sleep(1)

    element = Press(locate_AppraisalMethod, attribute_xpath)
    sleep(1)
    element = Press(locate_internet, attribute_xpath)

    element = Press(locate_RegistrationType, attribute_xpath)
    sleep(1)
    element = Press(locate_TitleTransfer, attribute_xpath)

    element = LocateByAttribute(attribute_xpath, locate_CreditReport)
    sleep(1)
    action.move_to_element(element).perform()
    sleep(1)
    element.click()
    sleep(5)


def CreditPreliminaryReport():
    locate_NegativeRemark = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[8]/div/app-credit-operations-report/app-sub-side-menu/div[2]/div[1]/app-scoring/div/div[2]/div/div/div/p-table/div/div/table/tbody/tr[12]/td[3]/p-dropdown/div/span'
    locate_age = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[8]/div/app-credit-operations-report/app-sub-side-menu/div[2]/div[1]/app-scoring/div/div[2]/div/div/div/p-table/div/div/table/tbody/tr[1]/td[3]/p-dropdown/div/div[2]/span'
    locate_61 = '/html/body/div/div/ul/p-dropdownitem[1]/li/span[1]'
    locate_TypeOfBiz = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[8]/div/app-credit-operations-report/app-sub-side-menu/div[2]/div[1]/app-scoring/div/div[2]/div/div/div/p-table/div/div/table/tbody/tr[3]/td[3]/p-dropdown/div/div[2]/span'
    locate_IPO = '/html/body/div/div/ul/p-dropdownitem[1]/li/span[1]'
    locate_position = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[8]/div/app-credit-operations-report/app-sub-side-menu/div[2]/div[1]/app-scoring/div/div[2]/div/div/div/p-table/div/div/table/tbody/tr[4]/td[3]/p-dropdown/div/div[2]/span'
    locate_specialist = '/html/body/div/div/ul/p-dropdownitem[1]/li/span[1]'
    locate_PeriodEmployment = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[8]/div/app-credit-operations-report/app-sub-side-menu/div[2]/div[1]/app-scoring/div/div[2]/div/div/div/p-table/div/div/table/tbody/tr[5]/td[3]/p-dropdown/div/div[2]'
    locate_Over5Y = '/html/body/div/div/ul/p-dropdownitem[1]/li/span[1]'

    locate_bankruptcy = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[8]/div/app-credit-operations-report/app-sub-side-menu/div[2]/div[1]/app-scoring/div/div[2]/div/div/div/p-table/div/div/table/tbody/tr[20]/td[3]/p-dropdown/div/span'
    locate_HirerNature = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[8]/div/app-credit-operations-report/app-sub-side-menu/div[2]/div[1]/app-scoring/div/div[2]/div/div/div/p-table/div/div/table/tbody/tr[14]/td[3]/p-dropdown/div/div[2]/span'
    locate_individual = '/html/body/div/div/ul/p-dropdownitem[1]/li/span[1]'
    locate_1stBuyerProject = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[8]/div/app-credit-operations-report/app-sub-side-menu/div[2]/div[1]/app-scoring/div/div[2]/div/div/div/p-table/div/div/table/tbody/tr[15]/td[3]/p-dropdown/div/div[2]/span'
    locate_N = '/html/body/div/div/ul/p-dropdownitem[1]/li'
    locate_DriverLicense = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[8]/div/app-credit-operations-report/app-sub-side-menu/div[2]/div[1]/app-scoring/div/div[2]/div/div/div/p-table/div/div/table/tbody/tr[16]/td[3]/p-dropdown/div/div[2]/span'
    locate_Y = '/html/body/div/div/ul/p-dropdownitem[2]'
    locate_BuyingPurpose = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[8]/div/app-credit-operations-report/app-sub-side-menu/div[2]/div[1]/app-scoring/div/div[2]/div/div/div/p-table/div/div/table/tbody/tr[17]/td[3]/p-dropdown/div/div[2]/span'
    locate_NonBusiness = '/html/body/div/div/ul/p-dropdownitem[1]/li/span[1]'

    locate_get = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[8]/div/app-credit-operations-report/app-sub-side-menu/div[2]/div[1]/app-scoring/div/div[1]/div/div/div/p-table/div/div/table/thead/tr/th[3]/div/button/span'
    locate_submit = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/sigv-fixed-bottom-panel/div/div/div/div/sigv-bpm-btn/div/button[1]/span'
    locate_CreditReport = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/ul/li[8]/a/span[1]'
    # locate_random = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div'
    action = ActionChains(driver)

    element = LocateByAttribute(attribute_xpath, locate_NegativeRemark)
    sleep(0.5)
    action.move_to_element(element).perform()
    sleep(1)

    element = Press(locate_age, attribute_xpath)
    sleep(1)
    element = Press(locate_61, attribute_xpath)

    element = Press(locate_TypeOfBiz, attribute_xpath)
    sleep(1)    
    element = Press(locate_IPO, attribute_xpath)

    element = Press(locate_position, attribute_xpath)
    sleep(1)
    element = Press(locate_specialist, attribute_xpath)

    element = Press(locate_PeriodEmployment, attribute_xpath)
    sleep(1)
    element = Press(locate_Over5Y, attribute_xpath)
    sleep(0.5)

    element = LocateByAttribute(attribute_xpath, locate_bankruptcy)
    sleep(0.5)
    action.move_to_element(element).perform()
    sleep(1)

    element = Press(locate_HirerNature, attribute_xpath)
    sleep(1)
    element = Press(locate_individual, attribute_xpath)

    element = Press(locate_1stBuyerProject, attribute_xpath)
    sleep(1)
    element = Press(locate_N, attribute_xpath)

    element = Press(locate_DriverLicense, attribute_xpath)
    sleep(1)
    element = Press(locate_Y, attribute_xpath)

    element = Press(locate_BuyingPurpose, attribute_xpath)
    sleep(1)
    element = Press(locate_NonBusiness, attribute_xpath)
    sleep(0.5)

    element = LocateByAttribute(attribute_xpath, locate_CreditReport)
    sleep(0.5)
    action.move_to_element(element).perform()
    sleep(1)
    element = Press(locate_get, attribute_xpath)
    sleep(1)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    
    element = Press(locate_submit, attribute_xpath)
    sleep(15)


def LogOut():
    locate_LogOutBlock = '/html/body/app-root/div[1]/sigv-layout/sigv-header/div/div[2]/button[2]'
    locate_LogOutButton = '/html/body/app-root/div[1]/sigv-layout/sigv-header/div/div[3]/div/div/button/span'

    element = Press(locate_LogOutBlock, attribute_xpath)
    sleep(1)
    element = Press(locate_LogOutButton, attribute_xpath)
    sleep(1)


def SM_Submit():
    locate_submit = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/sigv-fixed-bottom-panel/div/div/div/div/sigv-bpm-btn/div/button[1]/span'

    element = Press(locate_submit, attribute_xpath)
    sleep(10)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # sleep(1)




if __name__ == "__main__":

    ############################################################ Submission ####################################################################################
    # read excel and convert to dataframe
    file_path = '/Users/kian199887/Downloads/github_francistan88/DSA/automatic_testing/submission_information.xlsx'
    df = pd.read_excel(file_path)
    ID_isnull = df['IdNo'].isnull()
    column_name = {
        '0': 'Date',
        '1': 'CaseNo',
        '2': 'IdNo',
        '3': 'Guarantor Person(Indi)',
        '4': 'Guarantor Person(Corpo)',
        '5': 'Customer Name',
        '6': 'Mobile Phone',
        '7': 'CIF No(Corp)',
        '8': 'Status',
        '9': 'Product Name',
        '10': 'Attach pdf'
    } 

    # remove'.0' for all and add '0' in front of the Mobile Phone
    df = DataPreprocessing(df, ID_isnull)

    # log in part:
    login_email = 'nabiladibidris@chailease.com.my'
    CaseType = 'SC_Case'

    # Case related information:
    RowNo = 5
    row_data = df.iloc[RowNo]
    ID_No = int(df['IdNo'].iloc[RowNo])
    PersonalID = int(df['Guarantor Person(Indi)'].iloc[RowNo])
    CorporateID = df['Guarantor Person(Corpo)'].iloc[RowNo]
    CustomerName = df['Customer Name'].iloc[RowNo] 
    MobilePhone = df['Mobile Phone'].iloc[RowNo]
    
    # open the submission web 
    s = Service('./chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    # url = 'https://sit01-websubmission.chailease.com.my/websubmission-ui/'
    # driver.get(url)
    # time.sleep(3)

    # LogIn(login_email)    

    # CreateCase(CaseType)

    # FillCustomerInformation(ID_No)

    # FillEmployment()

    # FillGuarantorPerson(PersonalID, CorporateID, CustomerName, MobilePhone)

    # FillContactPerson()

    # FillCollateral()

    # FillTermsConditions()

    # FillAttachment()


    ############################################################# Preliminary Credit Review ####################################################################################
    # connect to SQL server
    server = 'tcp:misql-sigv-sit04.6c276a28d249.database.windows.net' 
    database = 'my_credit_rating_scales' 
    username = 'IBM_DBA' 
    password = 'IBM_DBA' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = cnxn.cursor()
    
    # get CaseNo, ApplicantId
    # by = 'IdNo'
    # CaseNo, CurrentApplicantId = GetSqlData(cursor, ID_No, by)
    # sleep(1)
    
    # write the case information to dataframe
    # df = AddCaseToDF(df, row_data, column_name, CaseNo)
    # print('\n\n')
    # print(df)
    # print('\n\n')
    
    # get credit officer's Email through API
    CurrentApplicantId = 'MY00329'
    CaseNo = 'H227000803VA2'
    api_url = f"http://10.164.55.100:8000/dev-backdoor/system-management/Rbac/UserProfile/{CurrentApplicantId}"
    OfficerEmail = 'MichaelLin@chailease.com.my.bak'

    # log in preliminary credit review
    credit_url = 'https://sit01-creditratingscales.chailease.com.my/creditratingscales-ui/'
    text_name = "Preliminary"

    driver.get(credit_url)
    sleep(6)

    Credit_LogIn(OfficerEmail)
    
    EnterIntoPCR(text_name)

    EnterCase(CaseNo)
    
    CreditInstructions()
 
    CreditCustomerInformation()

    new_file = '/Users/kian199887/Downloads/github_francistan88/DSA/automatic_testing/case_submission.xlsx'
    df.to_excel(new_file, index=False)
    
    CreditCollateral()

    CreditPreliminaryReport()


    ############################################################# Sales Manager Confirming Stage ####################################################################################
    # get CaseNo, ApplicantId
    by = 'CaseNo'
    CaseNo, CurrentApplicantId = GetSqlData(cursor, CaseNo, by)
    sleep(1)

    # get credit officer's Email through API
    api_url = f"http://10.164.55.100:8000/dev-backdoor/system-management/Rbac/UserProfile/{CurrentApplicantId}"
    OfficerEmail = GetApplicantEmail(api_url)

    # log in Sales Manager credit review
    text_name = "Sales"

    LogOut()

    Credit_LogIn(OfficerEmail)

    EnterIntoSM(text_name)

    EnterCase(CaseNo)

    SM_CreditInstructions()
    
    SM_Submit()


    ############################################################# Secondary Credit Review Stage ####################################################################################
    # # get CaseNo, ApplicantId
    # CaseNo, CurrentApplicantId = GetSqlData(cursor, CaseNo, by)
    # sleep(1)

    # # get credit officer's Email through API
    # api_url = f"http://10.164.55.100:8000/dev-backdoor/system-management/Rbac/UserProfile/{CurrentApplicantId}"
    # OfficerEmail = GetApplicantEmail(api_url)

    # # log in Sales Manager credit review
    # text_name = "Sales"

