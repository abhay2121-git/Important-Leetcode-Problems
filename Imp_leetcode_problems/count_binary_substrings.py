# Example 1:
# Input: s = "00110011"
# Output: 6

# Example 2:
# Input: s = "10101"
# Output: 4

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, cur = 0, 1
        res = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1

            else:
                prev = cur
                cur = 1

            if prev >= cur:
                res += 1

        return res