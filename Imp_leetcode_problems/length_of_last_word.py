# Example 1:
# Input: s = "Hello World"
# Output: 5

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                length += 1
            elif length > 0:
                break

        return length
    