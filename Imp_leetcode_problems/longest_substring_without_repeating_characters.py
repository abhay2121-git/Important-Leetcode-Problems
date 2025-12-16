
# Example 1:
# Input : s = "abcabcbb"
# Output : 3

# Example 2;
# Input : s = "bbbbb"
# Output : 1

class Solution:
    def __init__(self, s):
        self.s = s

    def longest_substring(self):
        l = 0
        longest = 0
        sett = set()
        n = len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            w = (r - l) + 1
            longest = max(longest, w)
            sett.add(s[r])
        return longest
    
s = "abcabcbb"
sol = Solution(s).longest_substring()
print(sol)


class Sol:
    def __init__(self):
        pass

    def longest_str(self, s):
        l = 0
        longest = 0
        sett = set()
        n = len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            w = (r - l) + 1
            longest = max(longest, w)
            sett.add(s[r])
        
        return longest

s = "pqrtsprt"
print(Sol().longest_str(s))
