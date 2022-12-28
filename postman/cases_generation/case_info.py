import csv
import pandas as pd

from pathlib import Path
from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    parser = ArgumentParser()

    # csv file from SQL server
    parser.add_argument('--input_path', type=Path, default='./case_db/input/Results.csv')
    
    # processed csv file
    parser.add_argument('--output_path', type=Path, default='./case_db/output/case_info.csv')

    # the range of cases' submissionId
    parser.add_argument('--upper_limit', type=int, default=None)
    parser.add_argument('--lower_limit', type=int, default=None)
    
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    csv_data = pd.read_csv(args.input_path)
    csv_data = csv_data[['CaseNo', 'CurrentApplicantId', 'SubmissionId']]
    filter_by_id = [int(i)<=args.upper_limit and int(i)>=args.lower_limit for i in csv_data['SubmissionId']]
    csv_data = csv_data[filter_by_id]
    csv_data.to_csv(args.output_path, index=False)

