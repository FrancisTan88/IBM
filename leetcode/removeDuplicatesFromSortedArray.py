class Solution:
    """
    Method1: Naive method (just delete it)

    Time complexity: O(N), given that N is the length of the list
    Space complexity: O(1)
    
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_val = nums[0]
        ind = 1
        while ind < len(nums):
            if nums[ind] == prev_val:
                nums.remove(prev_val)
            else:
                prev_val = nums[ind]
                ind += 1
        return ind


    """
    Method2: Take advantage of the property of "non-decreasing order"

    Time complexity: O(N), given that N is the length of the list
    Space complexity: O(1)
    
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[ind]:
                ind += 1
                nums[ind] = nums[i]
        return ind + 1 

    

