# Example 1:
# Input : n = 19
# Output : true

# Example 2:
# Input : n = 2
# Output : false

class Solution:
    def __init__(self, n):
        self.n = n

    def happynumber(self):
        seen = set()
        cur = str(n)

        while cur not in seen:
            seen.add(cur)
            summ = 0
            
            for digit in cur:
                digit = int(digit)
                summ += digit ** 2
            
            if summ == 1: 
                return True
            cur = str(summ)
        
        return False

n = 19
sol = Solution(n).happynumber()
print(sol)