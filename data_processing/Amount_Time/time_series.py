from cmath import nan
from itertools import count
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import math

"""
for task
"""

def FilterIBM(df):
    df_filter = df[~df['Created By'].str.contains('.ibm')]
    df_filter.reset_index(inplace=True)
    return df_filter


def TxtProcessing(data):
    # only keep yyyy/mm/dd
    for i in range(len(data)):
        data[i] = str(data[i]).split(" ")[0]
    data = pd.to_datetime(data)
    data = data.dt.strftime('%Y-%m')
    return data


# def KeepYearMonth(df):
#     # convert the data to pandas datetime
#     df['Created Date'] = pd.to_datetime(df['Created Date'])
#     # only keep YYYY-mm
#     df['Created Date'] = df['Created Date'].dt.strftime('%Y-%m')
#     return df


def CountByMonth(data):
    cum = 0
    dict = {}
    list_date = []
    list_count = []
    while cum < len(data):
        count = 1
        # cum = 1
        date = data[cum]
        cum += 1
        while cum < len(data) and data[cum] == date:
            count += 1
            cum += 1
        list_count.append(count)
        list_date.append(date)
    
    df = pd.DataFrame({
        'Date': list_date,
        'Tasks': list_count
    })
    # print(df)
    return df

if __name__ == '__main__':

    # read file and only keep Work Item Type, Created Date
    file_name = 'bug_filter.csv'
    read_file = pd.read_csv(file_name)
    # print(read_file)

    # drop '.ibm' and reset the index 
    df_filter = FilterIBM(read_file)
    # print(df_filter)
    
    # only keep the columns we want(Created Date) and rearrange the index
    df = pd.DataFrame(df_filter['Created Date'])

    # remove character and keep only yyyy-mm
    date_time = TxtProcessing(df['Created Date'])
    df['Created Date'] = date_time
    # print(df)

    # count occurrencies by months and make dataframe
    df_toPlot = CountByMonth(df['Created Date'])
    # print(df_toPlot)
    

    # plot it
    plt.plot(df_toPlot['Date'], df_toPlot['Tasks'])
    plt.xticks(rotation=45)
    plt.yticks(np.arange(0, max(df_toPlot['Tasks'])+1,15))
    plt.show()

