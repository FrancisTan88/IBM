class Solution:
    
    # stupid method:
    def romanToInt(self, s: str) -> int:    
        sum = 0
        curr_num = 0
        prev_num = 0
        # passit = False
        for i in range(len(s)):
            if s[i] == 'I':
                curr_num = 1
            elif s[i] == 'V':
                curr_num = 5
            elif s[i] == 'X':
                curr_num = 10
            elif s[i] == 'L':
                curr_num = 50
            elif s[i] == 'C':
                curr_num = 100
            elif s[i] == 'D':
                curr_num = 500
            elif s[i] == 'M':
                curr_num = 1000
                
            sum += curr_num
            
            if (prev_num == 1 and (curr_num == 5 or curr_num == 10)) or (prev_num == 10 and (curr_num == 50 or curr_num == 100)) or (prev_num == 100 and (curr_num == 500 or curr_num == 1000)):
                sum -= 2*prev_num
            
            prev_num = curr_num
        
        return sum
    

    # clever method: using hash map
    def romanToInt(self, s: str) -> int:
    
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        sum = 0
        # because it is guaranteed that the string is largest to small from left to right, so if there were exceptions, 
        # the cases must be (1,5), (10, 40), etc.
        # so if that way, just deduct the current number and we will get the right answer
        for i in range(len(s)):
            if i+1 <= len(s)-1 and map[s[i+1]] > map[s[i]]:  
                sum -= map[s[i]]
            else:
                sum += map[s[i]]
                
        return sum
                