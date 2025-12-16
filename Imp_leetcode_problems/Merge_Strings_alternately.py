# Merge String alternately
# Example 1:
# Input : word1 = "abc", word2 = "pqr"
# Output : "apbqcr"

# Example 2:
# Input : word1 = "ab", word2 = "pqrs"
# Output : apbqrs

class Solution:
    def __init__(self):
        pass

    def merge_strings_alternately(self, word1, word2):
        A, B = len(word1), len(word2)
        a, b = 0, 0
        s = []
        word = 1
        while a < A and b < B:
            if word == 1:
                s.append(word1[a])
                a += 1
                word = 2
            
            else:
                s.append(word2[b])
                b += 1
                word = 1
        
        while a < A:
            s.append(word1[a])
            a += 1
        
        while b < B:
            s.append(word2[b])
            b += 1
        
        return ''.join(s)

word1 = "abc"
word2 = "pqr"
sol = Solution().merge_strings_alternately(word1, word2)
print(sol)



# Another approach is 
class Sol:
    def __init__(self):
        pass

    def merge(self, word1, word2):
        i, j = 0, 0
        res = []

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        
        res.append(word1[i:])
        res.append(word2[j:])
        return ''.join(res)

word1 = "abc"
word2 = "pqr"
sol = Sol().merge(word1, word2)
print(sol)


class Merge:
    def __init__(self):
        pass

    def merge_str(self, word1, word2):
        A, B = len(word1), len(word2)
        a, b = 0, 0
        res = []

        word = 1
        while a < A and b < B:
            if word == 1:
                res.append(word1[a])
                a += 1
                word = 2
            else:
                res.append(word2[b])
                b += 1
                word = 1
        
        while a < A:
            res.append(word1[a])
            a += 1

        while b < B:
            res.append(word2[b])
            b += 1
        
        return "".join(res)

word1 = "abcd"
word2 = "pqrstuvw"
print(Merge().merge_str(word1, word2))