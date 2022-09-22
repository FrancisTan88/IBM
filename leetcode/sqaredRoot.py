class Solution:
    """
    Method: Naive
    Time complexity: O(n), given that n is the sqared root of x
    Space complexity: O(1)
    """
    def mySqrt(self, x: int) -> int:
        sqrt = 0
        while sqrt * sqrt <= x:
            sqrt += 1
        return sqrt - 1




    