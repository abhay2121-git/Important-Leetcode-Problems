# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_count[i] == window_count[i]:
                matches += 1

        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True

            right = ord(s2[i]) - ord('a')
            window_count[right] += 1
            if window_count[right] == s1_count[right]:
                matches += 1
            elif window_count[right] == s1_count[right] + 1:
                matches -= 1

            left = ord(s2[i - len(s1)]) - ord('a')
            window_count[left] -= 1
            if window_count[left] == s1_count[left]:
                matches += 1
            elif window_count[left] == s1_count[left] - 1:
                matches -= 1

        return matches == 26