import json
from typing import Dict
import pandas as pd
import numpy as np


def Read_jsonFile(file_path) -> Dict:
    with open(file_path, 'r') as json_file:
        to_dict = json.load(json_file)
        # values = list(to_dict['values'])
        return to_dict


# def ReverseKeyAndValue(variables) -> Dict:
#     dict = {}
#     for vars in variables:
#         key = vars['key']
#         value = vars['value']
#         dict[value] = key
#     return dict


def Iterate(dictionary) -> Dict:
    dict_tmp = {}
    for key, value in dictionary.items(): 
        # the current value is a list and is not empty
        if isinstance(value, list) and value:
            for i in range(len(value)):
                subDict = Iterate(value[i])
                dict_tmp[key] = subDict
            continue  # avoid executing the whole list again

        # the current value is a substring
        if isinstance(value, dict):
            subDict = Iterate(value)
            dict_tmp[key] = subDict
            continue  # avoid dictionary the whole list again
        
        dict_tmp[key] = value

    return dict_tmp



if __name__ == '__main__':
    # read json file: environment variables from postman
    envVar_filePath = 'environmentVar.json'
    dict_envVar = Read_jsonFile(envVar_filePath)
    variables = dict_envVar['values']

    # environment variables 
    # reverse the keys and values so that we can search the values in O(1) every time
    # hashmap = ReverseKeyAndValue(variables)
    # print(hashmap)
    
    # traverse request body from payload and 
    # store it as a dictionary
    '''
    bug: json檔有很多key重複, 
    在function iterate裡concatenate兩個不同的dictionary時, 
    會有original keys被new keys覆蓋的情形
    '''
    reqBody_path = 'test copy.json'
    dict_reqBody = Read_jsonFile(reqBody_path)
    dict_reqBodyTraversal = Iterate(dict_reqBody)
    for k, v in dict_reqBodyTraversal.items():
        print('key: ' + str(k) + ' -> ' + 'value: ' + str(v))
    








        
      

            