class Solution:
    """
    Advanced method:
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind, val in enumerate(nums):
            hashmap[val] = ind
        for ind, val in enumerate(nums):
            complement = target - val
            if complement in hashmap and ind != hashmap[complement]:
                return [ind, hashmap[complement]]
                    