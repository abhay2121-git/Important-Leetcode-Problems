# Example 1:
# Input: n = 2
# Output: 2

# Example 2:
# Input: n = 3
# Output: 3

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, a+b
        
        return b

        if n == 1:
            return 1
        
        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, a+b
            
        return b