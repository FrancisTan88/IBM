import pandas as pd
import numpy as np
import json

from typing import Dict, List
from argparse import ArgumentParser, Namespace
from pathlib import Path
from jsondiff import diff

from dataset import Env_Dataset, Input_Dataset


LST1 = ["true", "false", "null"]
SPECIAL = {"idNo": ['891007777777', '800225777777', '556097-H']}


def add_var_and_write(json_file, key: str, value, env_variables: Dict, last_instance: bool) -> None:
    def whether_comma(json_file, last_instance) -> None:
        if last_instance:
            json_file.write("\n")
        else:
            json_file.write(",\n")

    def write_env_var(json_file, key: str, vlaue, last_instance: bool, double_quotes: bool) -> None:
        if double_quotes:
            json_file.write(f'"{key}": ' + '"{{' + vlaue + '}}"')
        else:
            json_file.write(f'"{key}": ' + '{{' + vlaue + '}}')
        whether_comma(json_file, last_instance)

    def write_normal(json_file, key: str, value, last_instance: bool, double_quotes: bool) -> None:
        value = json.dumps(value)
        if not double_quotes:
            value = value.strip('"')
        json_file.write(f'"{key}": {value}') 
        whether_comma(json_file, last_instance)

    # environment vars
    if key in env_variables:
        # no double quotes:
        if (type(value) == int or type(value) == bool) or \
            (type(value) == str and env_variables[key] in LST1) or \
                (isinstance(value, type(None)) and (env_variables[key] in LST1)):
            double_quotes = False

        # has double quotes
        else:
            double_quotes = True

        # special vars:
        if key == 'idNo' and value == SPECIAL["idNo"][1]: value = "idNo_G1"
        elif key == 'idNo' and value == SPECIAL["idNo"][2]: value = "idNo_G2"
        else: value = key
        write_env_var(json_file, key, value, last_instance, double_quotes)
    
    # normal vars
    else:
        # no double quotes
        if type(value) == int or type(value) == list or \
            type(value) == bool or isinstance(value, type(None)):
            double_quotes = False
            value = json.dumps(value)
        # has double quotes
        else:
            double_quotes = True
        write_normal(json_file, key, value, last_instance, double_quotes)
    
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

def parse_args() -> Namespace:
    parser = ArgumentParser()

    # environment variables
    parser.add_argument('--env_file', type=Path, default='./environment/postman_environment.json')
    
    # original request body
    parser.add_argument('--ori_file', type=Path, default='./application/submit.json')
    
    # output request body(dir)
    parser.add_argument('--output_dir', type=Path, default='./ckpt')
    parser.add_argument('--output_file', type=Path, default='application_submit.json')
    
    args = parser.parse_args()
    return args



if __name__ == '__main__':
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    env_data = Env_Dataset(args.env_file)
    input_data = Input_Dataset(args.ori_file)
    with open(args.output_dir / args.output_file, 'w') as file:
        file.write('{\n')
        traverse(file, input_data.data, env_data.data)
        file.write('\n}')


