# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from typing import List
class SOlution:
    def __init__(self):
        pass

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_length = min(len(s) for s in strs)

        for i in range(min_length):
            ch = strs[0][i]
            for s in strs[1:]:
                if s[i] != ch:
                    return strs[0][:i]
        return strs[0][:min_length]

