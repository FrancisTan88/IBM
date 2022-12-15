import pandas as pd
import numpy as np
import json

from typing import Dict, List

from argparse import ArgumentParser, Namespace
from pathlib import Path

from jsondiff import diff

LST1 = ["true", "false", "null"]


def read_json(file_path) -> Dict:
    with open(file_path, 'r') as json_file:
        to_dict = json.load(json_file)
        return to_dict


def env_var_to_dict(values: List) -> Dict:
    dict = {}
    for i in values:
        # if var is active
        if i['enabled']:
            dict[i['key']] = i['value']
    return dict


def add_var_and_write(json_file, key: str, value, env_variables: Dict, last_instance: bool) -> None:
    def whether_comma(json_file, last_instance) -> None:
        if last_instance:
            json_file.write("\n")
        else:
            json_file.write(",\n")
            
    def write_env_var(json_file, key: str, last_instance: bool, double_quotes) -> None:
        if double_quotes:
            json_file.write(f'"{key}": ' + '"{{' + key + '}}"')
        else:
            json_file.write(f'"{key}": ' + "{{" + key + "}}")
        whether_comma(json_file, last_instance)

    def write_normal(json_file, key: str, value, env_variables: Dict, last_instance: bool, double_quotes) -> None:
        if double_quotes:
            value = json.dumps(value)
        else:
            value = json.dumps(value).strip('"')
        json_file.write(f'"{key}": {value}') 
        whether_comma(json_file, last_instance)
    
    if key in env_variables:
        # no double quotes:
        if (type(value) == int or type(value) == bool) or \
            (type(value) == str and env_variables[key] in LST1) or \
                (isinstance(value, type(None)) and (env_variables[key] in LST1)):
            double_quotes = False

        # has double quotes
        else:
            double_quotes = True
        write_env_var(json_file, key, last_instance, double_quotes)
    else:
        # no double quotes
        if type(value) == int or type(value) == list or \
            type(value) == bool or isinstance(value, type(None)):
            double_quotes = False
            value = json.dumps(value)
        # has double quotes
        else:
            double_quotes = True
        write_normal(json_file, key, value, env_variables, last_instance, double_quotes)
    

def traverse(json_file, request_body: Dict, env_var: Dict) -> None:
    last_instance = False
    for key, value in request_body.items():
        # first check if last instance
        if key == list(request_body.keys())[-1]:
            last_instance = True

        # current value is a subdict
        if isinstance(value, dict):
            json_file.write(f'"{key}": ' + "{\n")
            traverse(json_file, value, env_var)
            if last_instance:
                json_file.write("}\n")
                last_instance = False
            else:
                json_file.write("},\n")
            continue
        
        # current value is a sublist
        if isinstance(value, list) and value:
            # if value is something like [1,2,3]
            if False not in [type(i) == int for i in value]: 
                pass
            else:
                json_file.write(f'"{key}": ' + "[\n")
                for i in range(len(value)):
                    json_file.write("{\n")
                    traverse(json_file, value[i], env_var)
                    # last instance in list should not end with comma
                    if i == len(value)-1:
                        json_file.write("}\n")
                    else:
                        json_file.write("},\n")
                if last_instance:
                    json_file.write("]\n")
                    last_instance = False
                else:
                    json_file.write("],\n")
                continue  

        add_var_and_write(json_file, key, value, env_var, last_instance)


def print_dict(dict) -> None:
    for k, v in dict.items():
        print(f"key: {k} -> value: {type(v)}")


def parse_args() -> Namespace:
    parser = ArgumentParser()

    # environment variables
    parser.add_argument('--env_file', type=Path, default='./environment/environment_vars.json')
    
    # original request body
    parser.add_argument('--ori_file', type=Path, default='./application/submit.json')
    
    # output request body(dir)
    parser.add_argument('--output_dir', type=Path, default='./ckpt')
    parser.add_argument('--output_file', type=Path, default='application_submit.json')
    
    args = parser.parse_args()
    return args





if __name__ == '__main__':
    # get args
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True) # make dir if it doesn't exist

    # read json file: environment variables from postman
    dict_values = read_json(args.env_file)
    values = dict_values['values']
    dict_env_var = env_var_to_dict(values)
    
    # add environment variables to original request body and 
    # store it as a dictionary
    ori_req_body = read_json(args.ori_file)
    with open(args.output_dir / args.output_file, 'w') as json_file:
        json_file.write('{\n')
        traverse(json_file, ori_req_body, dict_env_var)
        json_file.write('\n}')

# first stage credit
# python3 ./find_difference.py --ori_file credit/firstStage/submit.json --output_file FC_submit.json



