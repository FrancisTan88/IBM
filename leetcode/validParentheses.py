class Solution:
    """
    Algo: using hash map and stack

    Time Complexity: O(N)
    Space Complexity: O(N)

    """
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        
        hashmap = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for i in s:
            if i in hashmap:
                stack.append(i)
                continue
            elif not stack or hashmap[stack[-1]] != i:
                return False
            stack.pop()
        return not stack

        