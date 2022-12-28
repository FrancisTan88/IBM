import json

# tmp = [1,2,"a"]
# print([type(i) == int for i in tmp])

# tmp = "K\t"
# print(tmp, "p")
# print(json.dumps(tmp).strip('"'))

with open('./application/submit.json', 'r') as file:
    load_it = json.load(file)
for k, v in load_it.items():
    # if k == 'lending':
    #     break
    print(type(v))

lst = []
lst2 = [1,2,3]
lst.append(lst2)
print(lst)