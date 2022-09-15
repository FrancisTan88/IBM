import random



def searchInsert(nums, target, start, end):
    middle = (start + end) // 2
    if start >= end:
        if target <= nums[start]: return start
        else: return start+1
    
    if target == nums[middle]:
        return middle
    elif target < nums[middle]:
        return searchInsert(nums, target, start, middle-1)
    elif target > nums[middle]:
        return searchInsert(nums, target, middle+1, end)


test_times = int(input())
print('')
for i in range(test_times):
    # gen random number from 1~100
    ran_list = sorted(random.sample(range(1, 101), 10)) 
    t = random.randint(1, 100) 
    print(ran_list)
    print(t)

    ind = searchInsert(ran_list, t, 0, len(ran_list)-1)
    print(ind)
    # print('\n')



