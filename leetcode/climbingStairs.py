import math
class Solution:
    """
    Method: arrangement and combination(排列組合)
    Time complexity: O(n^2), which n is the value given by the question 
    Space complexity: O(1)
    """
    def climbStairs(self, n: int) -> int:
        # count how many '2' at most
        count_two = 0
        clone_n = n
        while clone_n - 2 >= 0:
            count_two += 1
            clone_n -= 2
        
        # 排列組合
        num = 0
        while count_two >= 0:
            amount_one = n - 2*count_two
            amount_total = count_two + amount_one #total amount of numbers in line
            
            total_fact = math.factorial(amount_total)
            two_fact = math.factorial(count_two)
            one_fact = math.factorial(amount_one)
                
            num += total_fact / (two_fact*one_fact)
            
            count_two -= 1
        
        return int(num)


