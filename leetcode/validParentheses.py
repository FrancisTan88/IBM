class Solution:
    """
    Algo: using stack

    Time Complexity: O(N)
    Space Complexity: O(N)

    """
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                tmp = stack.pop()
                if (s[i] == ')' and tmp != '(') or (s[i] == ']' and tmp != '[') or (s[i] == '}' and tmp != '{'):
                    return False
                
        if stack:
            return False
        return True


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