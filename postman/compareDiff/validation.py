import json

# tmp = [1,2,"a"]
# print([type(i) == int for i in tmp])

# tmp = "K\t"
# print(tmp, "p")
# print(json.dumps(tmp).strip('"'))

# x = "aa bb cc"
# print(" ".join(x))

tmp = [
    {'key': 1,
     'value': 2,
     'y': True 
    },
    {
        'key': 3,
        'value': 4,
        'y': False
    }  
]

dict = {i['key']: i['value'] for i in tmp if i['y'] == True}
print(dict)