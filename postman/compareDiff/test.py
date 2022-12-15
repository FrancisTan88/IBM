from dataset import Dataset


env_path = './environment/postman_environment.json'
ori_path = './application/submit.json'

datasets = Dataset(env_path, ori_path)
# datasets.print_dict()
# print(datasets['dateManufacture'])
print(len(datasets.env_vars))
