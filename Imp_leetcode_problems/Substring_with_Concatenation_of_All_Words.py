from collections import Counter
class Solution:
    def findSubstring(self, s: str, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result = []
    
        for offset in range(word_len):
            left = offset
            right = offset
            seen = Counter()
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    seen[word] += 1

                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len

                    if right - left == total_len:
                        result.append(left)
                else:
                    seen.clear()
                    left = right
        
        return result