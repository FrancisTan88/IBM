class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Naive method:
        # Time complexity: O(N), given that N is the length of the list 
        # Space complexity: O(1)
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
        if count == 0:
            return len(nums)
        for j in range(count):
            nums.remove(val)
        return len(nums)
        
        
        # Advanced method: 
        # Time complexity: O(N), given that N is the length of the list
        # Space complexity: O(1)
        if val > 50:
            return len(nums)
        ind = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ind] = nums[i]
                ind += 1
        return ind