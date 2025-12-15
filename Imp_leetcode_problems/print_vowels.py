class VowelFinder:
    def __init__(self, text):
        self.text = text
    
    def find_vowels(self):
        vowels = []
        for char in self.text:
            if char in self.text:
                if char in "aeiou":
                    vowels.append(char)
        return vowels
text = "The quick brown fox jumps over the lazy dog"
vowel_finder = VowelFinder(text)
vowels = vowel_finder.find_vowels()
print(vowels)


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
