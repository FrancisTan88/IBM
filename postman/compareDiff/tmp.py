dict1 = {
    'a': '{{1}}',
    'b': 2
}
dict2 = {
    'b': '{{3}}',
    'c': 4
}
# d = dict1
# d.update(dict2)
# print(d)

for k, v in dict1:
    # if '{{}}' in v:
    print(k , v)
# print(dict1)