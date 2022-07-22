import pandas as pd
import pyodbc
import requests
import json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def GetEmailFromJson(obj):
    return obj['email']


def GetSqlData(cursor):
    # cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    # cursor = cnxn.cursor()
    SQL_data = cursor.execute(f"""select CaseNo, CreateTime, CurrentApplicantId, StatusID, StageId, ApplyDate, IdNo, ProductCode from CreditRatingScales.Submission
                    where IdNo = '{ID_No}' 
                    ORDER BY CreateTime DESC
                    """).fetchone()
    CaseNo = SQL_data[0]
    CurrentApplicantId = SQL_data[2]
    return CaseNo, CurrentApplicantId
    # print(CaseNo)

def GetApplicantEmail(url):
    response = requests.get(url)
    json_data = response.json()
    email = GetEmailFromJson(json_data)
    return email



# connect to SQL server
server = 'tcp:misql-sigv-sit04.6c276a28d249.database.windows.net' 
database = 'my_credit_rating_scales' 
username = 'IBM_DBA' 
password = 'IBM_DBA' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()   
ID_No = '970118123456'
CaseNo = 'H227000758VA2'

# get CaseNo, ApplicantId
# SQL_data = cursor.execute(f"""select CaseNo, CreateTime, CurrentApplicantId, StatusID, StageId, ApplyDate, IdNo, ProductCode from CreditRatingScales.Submission
#                 where IdNo = '{ID_No}' 
#                 ORDER BY CreateTime DESC
#                 """).fetchone()
CaseNo, CurrentApplicantId = GetSqlData(cursor)

# print(SQL_data)
# CaseNo = SQL_data[0]
# CurrentApplicantId = SQL_data[2]
print(CaseNo, CurrentApplicantId)
# get credit officer's Email through API
# api_url = f"http://10.164.55.100:8000/dev-backdoor/system-management/Rbac/UserProfile/{CurrentApplicantId}"
# OfficerEmail = GetApplicantEmail(api_url)

# print(data)
# print(OfficerEmail, CaseNo, CurrentApplicantId)


