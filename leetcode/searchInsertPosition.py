# Aka Binary search:

class Solution:
    """
    Method: Binary search (iteration)
    Time complexity: O(log n)
    Space complexity: O(1)
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start < end:
            mid = (end+start) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
            
        if target > nums[start]: return start + 1
        else: return start

    """
    Method: Binary search (recursive)
    Time complexity: O(log n)
    Space complexity: O(1)
    """
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


       


