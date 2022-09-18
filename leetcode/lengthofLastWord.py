class Solution:
    """
    Method: Naive method
    Time complexity: O(N), given that N is the lenth of the string
    Space complexity: O(1)

    """
    def lengthOfLastWord(self, s: str) -> int:
        ind = len(s)-1
        count = 0
        while ind >= 0:
            if s[ind] == ' ' and count != 0:
                break
            if s[ind] != ' ':
                count += 1
            ind -= 1 
        return count


    """
    Method: Clear method
    Time complexity: O(N), given that N is the lenth of the string
    Space complexity: O(N), given that N is the lenth of the new string
    """
    def lengthOfLastWord(self, s: str) -> int:
        new_s = s.split()
        return len(new_s[-1])




# num = ','.join(str(123)).split(',')
# print(num)


