# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.



class Solution:
    def __init__(self):
        pass

    def rom_to_int(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        summ = 0
        n = len(s)
        i = 0
        
        while i < n:
            if i < n -1 and d[s[i]] < d[s[i+1]]:
                summ += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                summ += d[s[i]]
                i += 1
        
        return summ

s = "MCMXCIV"
print(Solution().rom_to_int(s))


class Roman:
    def __init__(self):
        pass

    def rom_to_intt(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        summ = 0
        n = len(s)
        i =  0

        while i < n:
            if i < n - 1 and d[s[i]] < d[s[i+1]]:
                summ += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                summ += d[s[i]]
                i += 1
        
        return summ

s = "XVI"
print(Roman().rom_to_intt(s))