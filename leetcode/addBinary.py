class Solution:
    """
    Method: Sum the two numbers first, and process the carrying digits problems after
    Time complexity: 很大的O(n)
    Space complexity: O(n)
    """
    def addBinary(self, a: str, b: str) -> str:
        # calculate the sum of two
        # convert it to string list and turn the dtype into int
        addition = ','.join(str(int(a) + int(b))).split(',')
        addition = [int(x) for x in addition]
        
        # process the carry digits
        ind = len(addition)-1
        while ind >= 1:
            if addition[ind] >= 2:
                addition[ind-1] += 1
                addition[ind] -= 2
            ind -= 1
        
        # check and process the first digits
        # if the first digit needs to be carried, the length of string would change
        if addition[0] >= 2:
            addition[0] -= 2
            addition = [1] + addition
        
        # return the resulting string
        string = ''
        for i in addition:
            string += str(i)
        return string
    
    
    """
    Method: Using the properties of Arithmetic: %, //
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def addBinary(self, a: str, b: str) -> str:
        aL, bL = -len(a), -len(b)
        i, carry, res = -1, 0, ""

        while i >= aL or i >= bL:
            aBit = int(a[i]) if i >= aL else 0
            bBit = int(b[i]) if i >= bL else 0
            
            sum = aBit + bBit + carry
            res = str(sum % 2) + res
            carry = sum // 2

            i -= 1
            
        return "1" + res if carry else res