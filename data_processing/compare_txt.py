
# reading files
# f1 = open("DML_Ru.txt", "r")  
# f2 = open("test.txt", "r")  
  
with open("DML_Ru.txt", 'r') as ori_file:
    lines1 = ori_file.readlines()

with open("test.txt", 'r') as new_file:
    lines2 = new_file.readlines()

# check if the schema are identity
# num_sch1 = 0
# for l1 in lines1:
#     if "SET" in l1:
#         num_sch1 += 1
# num_sch1 /= 2

# num_sch2 = 0
# for l2 in lines2:
#     if "SET" in l2:
#         num_sch2 += 1
# num_sch2 /= 2

key_word = "INSERT"
list1 = []
list2 = []
isSET = "SET"
isOFF = 'OFF'
count1 = 0
count2 = 0
# for i in range(24):
#     num_insert = 0
for l1 in lines1:
    # if isOFF in l1:
    #     list1.append(count1)
    #     count1 = 0
    if isSET not in l1 and key_word in l1 and "VALUES" in l1:
        count1 += 1

for l2 in lines2:
    # if isOFF in l2:
    #     list2.append(count2)
    #     count2 = 0
    if isSET not in l2 and key_word in l2  and "VALUES" in l2:
        count2 += 1

print(count1, count2)
# print(len(list1))
# print(list1, '\n')
# print(len(list2))
# print(list2, '\n')


# str = "INSERT [collection].[AssignRuleSetting] ([AssignRuleSettingId], [ProcessStage], [OverdueFrom], [OverdueTo], [DispatchRuleId], [SortNo]) VALUES (1,  1,  NULL,  30,  1,  1)"
# if isSET not in str and key_word in str:
#     print("fuck")
# print(num_sch1, num_sch2)  # (24, 24)


# i = 0
  
# for line1 in f1:
#     i += 1
      
#     for line2 in f2:
          
#         # matching line1 from both files
#         if line1 == line2:  
#             # print IDENTICAL if similar
#             # print("Line ", i, ": IDENTICAL")    
#             pass   
#         else:
#             print("Line ", i, ":")
#             # else print that line from both files
#             print("\tFile 1:", line1, end='')
#             print("\tFile 2:", line2, end='')
#         break