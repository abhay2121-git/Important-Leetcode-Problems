# InterviewBit question
class Solution:
    def __init__(self):
        pass
    
    def find_vowelss(self, text):
        vowels = []
        for char in text:
            if char in text:
                if char in "aeiou":
                    vowels.append(char)
        return vowels

text = "The quick brown fox jumps over the lazy dog"
vowel_finder = Solution().find_vowelss(text)
print(vowel_finder)
