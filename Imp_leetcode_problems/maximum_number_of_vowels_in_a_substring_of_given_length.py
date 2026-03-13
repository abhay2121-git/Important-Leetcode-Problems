# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3

# Example 2:
# Input: s = "aeiou", k = 2
# Output: 2

# Example 3:
# Input: s = "leetcode", k = 3
# Output: 2

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        curr = sum(1 for c in s[:k] if c in vowels)
        max_vowels = curr

        for i in range(k, len(s)):
            if s[i] in vowels:
                curr += 1
            
            if s[i - k] in vowels:
                curr -= 1

            max_vowels = max(max_vowels, curr)

        return max_vowels
