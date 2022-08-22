

str1 = "8269, 12, CAST(N'2022-08-01T00:00:00.000' AS DateTime), N'M2', N'MY00326', 1, N'A', CAST(1.00000000 AS Decimal(12, 8)), CAST(N'2022-07-05T11:02:50.640' AS DateTime), N'System'"
str2 = 'AAA apple'

list = []
list2= [0, 0, 0]
list3= [1, 1, 1]
val = str1.split(", ")
list.append(val)

list_coll = [val, list2, list3]
print(list_coll)
# print(list)
# print(list[0])
# print(list[1])
# print(len(val))

# for i in range(len(val)):
#     if i >= len(val):
#         break
#     if ")" in val[i] and "(" not in val[i]:
#         val.remove(val[i])
#         i -= 1
#         print(i)
#         print(len(val))
#         print(val[i+1])

# print(val)