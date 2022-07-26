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
# from AT_SC0011_13to15 import Credit_LogIn, EnterCase, EnterIntoPCR, LocateByText

attribute_xpath = 'xpath'


def LocateByText(locate_name, text_name):
    text_name = '"' + text_name + '"'
    element = driver.find_element(By.XPATH, locate_name + f'//*[contains(text(), {text_name})]')
    return element


def LocateByAttribute(attribute, locate_name):
    if attribute == 'id':
        element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locate_name)))

    elif attribute == 'class':
        element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, locate_name)))

    elif attribute == 'xpath':
        element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locate_name)))
    
    elif attribute == 'css':
        element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, locate_name)))

    return element2


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


def Credit_LogIn(OfficerEmail):
    locate_e = '//*[@id="userEmail"]'
    credit_login = '/html/body/app-root/div[1]/sigv-login/div[1]/form/div[2]/button'
    element = Type(locate_e, OfficerEmail, attribute_xpath)
    sleep(1)
    element = Press(credit_login, attribute_xpath)
    sleep(3)

def EnterIntoPCR(text_name):
    locate_main = '//*[@id="p-accordiontab-0-content"]/div'
    element = LocateByText(locate_main, text_name)
    sleep(1)
    element.click()
    sleep(5)


def EnterCase(text_name):
    locate_body = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-todo-list/sigv-data-table/div/p-table/div/div[2]/div/div[2]'
    element = LocateByText(locate_body, text_name)
    sleep(0.5)
    element.click()
    sleep(10)


def CreditInstructions():
    locate_CreditInstructions = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/ul/li[2]/a/span[1]'
    locate_CreditComment = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[2]/div/app-credit-instructions/div/div[1]/div/div/p-dropdown/div/div[2]/span'
    locate_recommend = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[2]/div/app-credit-instructions/div/div[1]/div/div/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li'
    locate_InstructionsBlock = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[2]/div/app-credit-instructions/div/div[2]/app-instruction/div/div/div[2]/div/textarea'
    locate_decision = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[2]/div/app-credit-instructions/div/div[2]/app-instruction/div/div/div[2]/div/div'
    locate_random = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[2]/div/app-credit-instructions/div/div[1]'
    locate_CustomerInformation = '//*[@id="version-comparison_customer-information"]'
    text_name = 'Approval'
    action = ActionChains(driver)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    element = Press(locate_CreditInstructions, attribute_xpath)
    sleep(1)
    element = Press(locate_CreditComment, attribute_xpath)
    sleep(1)
    element = Press(locate_recommend, attribute_xpath)
    # sleep(1)
    element = Press(locate_InstructionsBlock, attribute_xpath)
    sleep(0.5)
    element = LocateByText(locate_decision, text_name)
    sleep(0.5)
    element.click()
    sleep(0.5)
    element = Press(locate_random, attribute_xpath)
    sleep(1)
    element = Press(locate_CustomerInformation, attribute_xpath)
    sleep(1)
    

def CreditCustomerInformation():
    locate_EducationLvl = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[3]/div/app-credit-operations-information/div[2]/app-information-individual/div[1]/div[4]/div[1]/div/div/p-dropdown/div/div[2]/span'
    locate_master = '/html/body/div/div/ul/p-dropdownitem[1]/li/span[1]'
    locate_LengthOfResidence = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[3]/div/app-credit-operations-information/div[2]/app-information-individual/div[1]/div[4]/div[3]/div/div/p-inputnumber/span/input'
    locate_collateral = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/ul/li[6]/a/span[1]'
    locate_random = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[3]/div/app-credit-operations-information/div[2]/app-information-individual/div[2]/div[3]/div[1]/div'
    locate_MobilePhone2 = '/html/body/app-root/div[1]/sigv-layout/div/div/div/app-credit-operations-detail/p-tabview/div/div/p-tabpanel[3]/div/app-credit-operations-information/div[2]/app-information-individual/div[2]/div[1]/div[2]/div/app-phone/div[2]/input' 
    LengthOfResidence = 1
    action = ActionChains(driver)


    element = LocateByAttribute(attribute_xpath, locate_MobilePhone2)
    sleep(1)
    action.move_to_element(element).perform()
    sleep(1)
    element = Press(locate_EducationLvl, attribute_xpath)
    sleep(1)
    
    element = Press(locate_master, attribute_xpath)
    sleep(0.5)
    element = Type(locate_LengthOfResidence, LengthOfResidence, attribute_xpath)
    sleep(0.5)
    element = Press(locate_collateral, attribute_xpath)
    sleep(5)


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
    sleep(3)


def CreditReport():
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
    sleep(10)


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




if __name__ == "__main__":

    CaseNo = 'H227000782VA2'
    OfficerEmail = 'Azela@chailease.com.my'
    sleep(1)

    # log in preliminary credit review
    credit_url = 'https://sit01-creditratingscales.chailease.com.my/creditratingscales-ui/'
    text_name = "Preliminary"

    s = Service('./chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get(credit_url)
    sleep(5)


    Credit_LogIn(OfficerEmail)
    
    EnterIntoPCR(text_name)

    EnterCase(CaseNo)

    CreditInstructions()

    CreditCustomerInformation()

    CreditCollateral()

    CreditReport()


############################################################# Sales Manager Confirming Stage ####################################################################################
    # get CaseNo, ApplicantId
    by = 'CaseNo'
    CaseNo, CurrentApplicantId = GetSqlData(cursor, CaseNo, by)
    sleep(2)

    # get credit officer's Email through API
    api_url = f"http://10.164.55.100:8000/dev-backdoor/system-management/Rbac/UserProfile/{CurrentApplicantId}"
    OfficerEmail = GetApplicantEmail(api_url)
    sleep(1)

    # log in Sales Manager credit review
    text_name = "Sales Manager Confirming Stage"

    driver.get(credit_url)
    sleep(5)

    Credit_LogIn(OfficerEmail)

    EnterIntoPCR(text_name)

    EnterCase(CaseNo)
    


