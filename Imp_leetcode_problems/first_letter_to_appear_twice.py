# Given a string s consisting of lowercase English letters, return the first letter to appear twice.
# Note:
# A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
# s will contain at least one letter that appears twice.
 
# Example 1:
# Input: s = "abccbaacz"
# Output: "c"


# Brute-force linear search
class Solution:
    def __init__(self):
        pass

    def appear_twice(self, s):
        seen_letters = []
        for c in s:
            if c in seen_letters:
                return c
            else:
                seen_letters.append(c)

s = "abccbaacz"
print(Solution().appear_twice(s))

# first_letter_to_appear_twice

