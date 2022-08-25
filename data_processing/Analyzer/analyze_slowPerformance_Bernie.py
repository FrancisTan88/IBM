import logging
import pandas as pd
import numpy as np
from datetime import datetime


def toMilliseconds(time):
    t = time.split(".")
    d = datetime.strptime(t[0], '%Y-%m-%d %H:%M:%S').timestamp() * 1000 +float("0."+t[1])*1000
    return d

file_name = "log.txt"
data = pd.read_csv(file_name, sep='|', header=None)
original_df = pd.DataFrame(data)
empty_df = pd.DataFrame(columns=["Time", "Space", "Interval", "Action", "Time took", "Command"])

print(data)


str_send = ' Sending HTTP request '
str_receive =' Received HTTP response ' 
str_exe = 'Executed DbCommand'
pt = 0
for i in range(len(original_df)):
    tmp_row_data = original_df.iloc[i]
    condition_exe = tmp_row_data.str.contains(str_exe, na=False)
    condition_receive = tmp_row_data.str.contains(str_receive, na=False)
    condition_send = tmp_row_data.str.contains(str_send, na=False)
    print(condition_exe)

    if condition_exe[6]:
        date_time = tmp_row_data[0]  # A
        mt = toMilliseconds(date_time)
        dt = int(mt-pt) if pt>0 else 0  # B
        exet = str(tmp_row_data[6][tmp_row_data[6].index("(")+1:tmp_row_data[6].index(")")-2]).replace(",", "")     # E
        interval = dt - float(exet) #C
        action = "DB"  # D
        command = str(tmp_row_data[6]).replace("Executed DbCommand ("+str(exet)+"ms) ","")  # F
        empty_df.loc[len(empty_df)] = [date_time, dt, interval, action, int(exet), command]
        pt = mt

    elif condition_send[6]:
        req = str(tmp_row_data[6]).replace(str_send, "")
    
    elif condition_receive[6]:
        date_time = tmp_row_data[0]  # A
        mt = toMilliseconds(date_time)
        dt = int(mt-pt) if pt>0 else 0  # B
        t = str(tmp_row_data[6]).replace(str_receive, "").replace("headers after ","").replace("ms - 200","").replace("ms - 201","").replace("ms - 400","")
        interval = dt - float(t)  # C
        action = "API"  # D
        exet = float(t)  # E
        command = req  #  F
        empty_df.loc[len(empty_df)] = [date_time, dt, interval, action, exet, command]
        pt = mt

empty_df.to_excel(excel_writer="/Users/kian199887/Downloads/Bernie_python/fff.xlsx")
