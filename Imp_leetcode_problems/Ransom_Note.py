# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Approach 1
        # return not (Counter(ransomNote) - Counter(magazine))

        # Approach 2
        count = [0] * 26

        for char in magazine:
            count[ord(char) - ord('a')] += 1

        for char in ransomNote:
            count[ord(char) - ord('a')] -= 1

            if count[ord(char) - ord('a')] < 0:
                return False
            
        return True