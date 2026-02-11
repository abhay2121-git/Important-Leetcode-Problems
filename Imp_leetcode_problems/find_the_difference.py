# Example 1:
# Input: s = "abcd", t = "abcde"
# Output: "e"

# Example 2:
# Input: s = "", t = "y"
# Output: "y"

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0

        for char in s:
            result ^= ord(char)
        
        for char in t:
            result ^= ord(char)

        return chr(result)