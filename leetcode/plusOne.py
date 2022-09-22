class Solution:
    """
    Method1: Convert the List into integer -> Calculate it -> Trun back to list and return
    Time complexity: O(N^2), given that N is the length of the list
    Space complexity: O(N), given that N is the space of the returned list
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        d = len(digits)-1
        value = 0
        ind = 0
        # calculate the value
        while ind <= len(digits)-1:
            value += 10**d * digits[ind]
            d -= 1
            ind += 1
        
        string = str(value+1)  # int to str time complexity is about: theta(n^2)
        ret_list = []
        for i in string:
            ret_list.append(i)
        
        return ret_list
    

    """
    Method2: Processing the carry digits problems (average performance is better than that of Method1)
    Time complexity: O(N), given that N is the length of the list
    Space complexity: O(N), given that N is the space of the returned list
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        ind = len(digits)-1
        while ind >= 0:
            if digits[ind] < 9:
                digits[ind] += 1
                return digits
            
            digits[ind] = 0
            ind -= 1
        
        return [1] + digits



    



        