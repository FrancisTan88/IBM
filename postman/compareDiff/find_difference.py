import pandas as pd
import numpy as np
import json

from ast import List
from typing import Dict

from argparse import ArgumentParser, Namespace
from pathlib import Path


def Read_jsonFile(file_path) -> Dict:
    with open(file_path, 'r') as json_file:
        to_dict = json.load(json_file)
        # values = list(to_dict['values'])
        return to_dict

def EnvVarToDict(values: List) -> Dict:
    dict = {}
    for i in values:
        # if var is active
        if i['enabled']:
            dict[i['key']] = i['value']
    return dict

def Iterate(dictionary, env_variables: Dict) -> Dict:
    dict_tmp = {}
    for key, value in dictionary.items(): 
        # the current value is a list and is not empty
        if isinstance(value, list) and value:
            tmp = []
            for i in range(len(value)):
                subDict = Iterate(value[i], env_variables)
                tmp.append(subDict)
            dict_tmp[key] = tmp
            continue  # avoid executing the whole list again

        # the current value is a substring
        if isinstance(value, dict):
            subDict = Iterate(value, env_variables)
            dict_tmp[key] = subDict
            continue  # avoid executing the whole list again
        
        # if environment variables
        if key in env_variables:
            # print('yes')
            value = '{{' + key + '}}'
            # value = value.strip('"')
            # print(value)
        dict_tmp[key] = value
        # print(type(value))

    return dict_tmp

def write_json(request_body: Dict, output_dir: Path) -> None:
    json_obj = json.dumps(request_body)
    output_file = 'var_req_body.json'
    with open(output_dir / output_file, 'w') as json_file:
        json_file.write(json_obj)

def print_dict(dict) -> None:
    for k, v in dict.items():
        print('key: ' + str(k) + ' -> ' + 'value:', v)

def parse_args() -> Namespace:
    parser = ArgumentParser()

    # environment variables
    parser.add_argument('--env_var_path', type=Path, default='./environment_variables.json')
    
    # original request body
    parser.add_argument('--ori_req_body', type=Path, default='./test.json')
    
    # output request body(dir)
    parser.add_argument('--output_req_body', type=Path, default='./ckpt/')

    args = parser.parse_args()
    return args



if __name__ == '__main__':
    # get args
    args = parse_args()
    args.output_req_body.mkdir(parents=True, exist_ok=True) # make dir if it doesn't exist

    # read json file: environment variables from postman
    dict_values = Read_jsonFile(args.env_var_path)
    values = dict_values['values']

    # convert values to dict
    dict_env_var = EnvVarToDict(values)
    # print_dict(dict_env_var)
    
    # add environment variables to original request body and 
    # store it as a dictionary
    ori_req_body = Read_jsonFile(args.ori_req_body)
    var_req_body = Iterate(ori_req_body, dict_env_var)
    # print_dict(dict_reqBodyTraversal)

    # write json
    write_json(var_req_body, args.output_req_body)




