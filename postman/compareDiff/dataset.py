import pandas as pd
import numpy as np
import json

from typing import Dict, List

from argparse import ArgumentParser, Namespace
from pathlib import Path

from jsondiff import diff


class Dataset():
    def __init__(self, env_vars_path: Path, ori_payload_path: Path) -> None:
        with open(env_vars_path, 'r') as file:
            load_env = json.load(file)
        with open(ori_payload_path, 'r') as file:
            load_payload = json.load(file)
        load_env = load_env['values']
        dict = {i['key']: i['value'] for i in load_env if i['enabled'] == True}
        self.env_vars = dict
        self.ori_payload = load_payload


    def __len__(self) -> int:
        return len(self.env_vars)


    def __getitem__(self, key: str) -> str:
        return self.env_vars[key]


    def print_dict(self) -> None:
        for k, v in self.env_vars.items():
            print(f"key: {k} -> value: {v}")






