class Solution:
    """
    Naive method: using two lists to store string forward and backward
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        list_forward = []
        list_backward = []
        for i in string:
            list_forward.append(i)
        for j in string[::-1]:
            list_backward.append(j)
        for k in range(len(string)):
            if list_forward[k] != list_backward[k]:
                return False
        return True

    """
    Naive method: using two inverse indexes to compare forward and backward 
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        ind_forward = 0
        ind_backward = len(string)-1
        while ind_forward < int(len(string)/2):
            if string[ind_forward] != string[ind_backward]:
                return False
            ind_forward += 1
            ind_backward -= 1
        return True

    """
    TODO
    Advanced method: Math algorithm
    Time complexity: O(log(n))
    Space complexity: O(1)
    """
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        revert = 0
        while x > revert:
            complement = x % 10
            revert = revert*10 + complement
            x = int(x/10)
        if revert == x or int(revert/10) == x:
                return True
        return False
            




