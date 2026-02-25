# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"

class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        n = len(s)
        i = n - 1

        while i >= 0:
            while i >= 0 and s[i] == ' ':
                i -= 1

            if i < 0:
                break

            j = i

            while i >= 0 and s[i] != ' ':
                i -= 1
            
            result.append(s[i + 1 : j + 1])
        
        return ' '.join(result)
