


class Solution:
    """
    Method: Vertical scanning
    
    Time complexity: O(N*M), given that there are N strings in list at most, and the length of every string is not longer than M
    Space complexity: O(1)

    For the first for loop, find the shortest string in the array, and store that string.
    For the double for loops, we take the character of the string we store before, 
    and using the inner for loop to go through the entire array to check if there is different character,
    if that way, we don't have to continue the iterations, just return the result,
    however, if the double for loops is finished and there still nothing to be returned, 
    it must mean that the result is the "string" itself.
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str = len(strs[0])
        string = strs[0]
        for i, s in enumerate(strs):
            if len(strs[i]) < shortest_str:
                shortest_str = len(strs[i])
                string = s
        
        ret_str = ""
        for i in range(shortest_str):
            curr_char = string[i]
            for j in range(len(strs)):
                if strs[j][i] != curr_char:
                    return ret_str
            ret_str = ret_str + curr_char
                    
        return ret_str


    """
    Method: Vertical scanning (improved)

    Time complexity: O(N*M), given that there are N strings in list at most, and the length of every string is not longer than M
    Space complexity: O(1)

    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(len(strs)):
                if i >= len(strs[j]) or char != strs[j][i]:
                    return strs[0][:i]
        return strs[0]


    """
    Tricky method: Get the most different two strings by the function min(), max() and find the longest common prefix of them

    Time Complexity: O(N*M), given that there are N strings in list at most, and the length of every string is not longer than M
                    -> function min(), max() scan all the characters in list 
    Space Complexity: O(1)

    function min() and max() will sort a string list by its alphabet, 
    Ex: S = ['aa', 'aac', 'aaf', 'ac', 'ad', 'aafz'],
    imagine the list is sorted: ['aa', 'aac', 'aaf', 'aafz', 'ac', 'ad']
    now min(S) == 'aa'and max(S) == 'ad',
    because the min(S) and max(S) are the most different two strings in list,
    comparing these two strings will represent all others.
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum = min(strs)
        maximum = max(strs)
        # count = 0
        for i in range(len(minimum)):
            if minimum[i] != maximum[i]:
                return minimum[:i]
        return minimum
  