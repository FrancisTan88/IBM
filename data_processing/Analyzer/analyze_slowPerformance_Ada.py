# from itertools import count
from email import header
from types import NoneType
import pandas as pd
import numpy as np
from datetime import datetime


# Convert datetime to milliseconds
def toMilliseconds(time):
    t = time.split(".")
    d = datetime.strptime(t[0], '%Y-%m-%d %H:%M:%S').timestamp() * 1000 +float("0."+t[1])*1000
    return d


# remove sqare brackets and split data correctly
def RemoveBrackets(df_log):
    for i in range(len(df_log)):
        df_log['log'].iloc[i] = str(df_log['log'].iloc[i]).strip("[]")
        df_log['log'].iloc[i] = df_log['log'].iloc[i].replace("][", " | ")

    df = df_log['log'].str.split('|', expand=True)
    return df


# Write data and export to excel file 
def WriteData(df, export_file_name, str_send, str_receive, str_exe):
    pt = 0
    req = 0
    for i in range(len(df)):
        tmp_row_data = df.iloc[i]  # pd.Series
        condition_exe = tmp_row_data.str.contains(str_exe, na=False)
        condition_receive = tmp_row_data.str.contains(str_receive, na=False)
        condition_send = tmp_row_data.str.contains(str_send, na=False)

        if condition_exe.any():
            ind = str(condition_exe.index[condition_exe].values).replace("[", "").replace("]", "")
            ind = int(ind)
            
            date_time = tmp_row_data[0]  # A
            mt = toMilliseconds(date_time)
            dt = int(mt-pt) if pt>0 else 0  # B
            string = str(tmp_row_data[ind])  # string
            exet = string[string.index("(")+1:string.index(")")-2].replace(",", "")     # E
            interval = dt - float(exet) #C
            action = "DB"  # D
            command = str(tmp_row_data[ind]).replace("Executed DbCommand ("+str(exet)+"ms) ","")  # F
            empty_df.loc[len(empty_df)] = [date_time, dt, interval, action, int(exet), command]
            pt = mt

        elif condition_send.any():
            ind = str(condition_send.index[condition_send].values).replace("[", "").replace("]", "")
            ind = int(ind)
            req = str(tmp_row_data[ind]).replace(str_send, "")
        
        elif condition_receive.any():
            if req == 0:
                req = '(No sending data before)'
            ind = str(condition_receive.index[condition_receive].values).replace("[", "").replace("]", "")
            ind = int(ind)
            date_time = tmp_row_data[0]  # A
            mt = toMilliseconds(date_time)
            dt = int(mt-pt) if pt>0 else 0  # B
            t = str(tmp_row_data[ind]).replace(str_receive, "").replace("headers after ","").replace("ms - 200","").replace("ms - 201","").replace("ms - 400","").replace("ms - 500", "")
            action = "API"  # D
            exet = float(t)  # E
            command = req  #  F
            empty_df.loc[len(empty_df)] = [date_time, dt, interval, action, exet, command]
            pt = mt

    empty_df.to_excel(excel_writer=export_file_name, index=False)


if __name__ == '__main__':

    # read the file and only keep column 'log'
    read_file = pd.read_csv('ada_time.csv')
    df_log = pd.DataFrame(read_file['log'])
    empty_df = pd.DataFrame(columns=["Time", "Space", "Interval", "Action", "Time took", "Command"])

    # remove sqare brackets and split data correctly
    df = RemoveBrackets(df_log)

    # write excel
    str_send = 'Sending HTTP request'
    str_receive =' Received HTTP response ' 
    str_exe = ' Executed DbCommand '
    
    export_file = 'UAT_BA_submission_slowPerformance_Ada.xlsx'
    WriteData(df, export_file, str_send, str_receive, str_exe)








