import pandas as pd
import numpy as np
import json

from typing import Dict, List

from argparse import ArgumentParser, Namespace
from pathlib import Path

from jsondiff import diff


class Env_Dataset():
    def __init__(self, env_vars_path: Path) -> None:
        with open(env_vars_path, 'r') as file:
            load_it = json.load(file)
        self.name = load_it['name']
        self.data = {i['key']: i['value'] for i in load_it['values'] if i['enabled'] == True}
    
    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, key: str) -> str:
        if key not in self.data:
            raise TypeError("The key is not in the postman environment variables")
        return self.data[key]
    
    def print_it(self) -> None:
        for k, v in self.data.items():
            print(f"key: {k} -> value: {v}")


class Input_Dataset():
    def __init__(self, ori_payload_path: Path) -> None:
        with open(ori_payload_path, 'r') as file:
            load_it = json.load(file)
        self.data = load_it
    
    def __len__(self) -> int:
        return len(self.data)

    def get_value(self, input_key: str, value) -> List:
        values = []
        for k, v in value.items():
            if k == input_key:
                values.append(v)
            if isinstance(v, dict):
                values += self.get_value(input_key, v)
            if isinstance(v, list) and v:
                # if value is something like [1,2,3]
                if False not in [type(i) == int for i in v]: 
                    pass
                else:
                    for instance in v:
                        values += self.get_value(input_key, instance)
        return values
    
    def print_it(self) -> None:
        for k, v in self.data.items():
            print(f"key: {k} -> value: {v}")