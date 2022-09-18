class Solution:
    """
    Method: Naive method
    Time complexity: O(N), given that N is the length of the list
    Space complexity: O(N), given that N is the space of the returned list
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        d = len(digits)-1
        value = 0
        ind = 0
        while ind <= len(digits)-1:
            value += 10**d * digits[ind]
            d -= 1
            ind += 1
        
        string = str(value+1)
        ret_list = []
        for i in string:
            ret_list.append(i)
        
        return ret_list
        
        