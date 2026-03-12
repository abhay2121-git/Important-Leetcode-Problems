# Example 1:
# Input: n = 5
# Output: 2

# Example 2:
# Input: n = 7
# Output: 0

# Example 3:
# Input: n = 10
# Output: 5

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        mask = 1
        while mask < n:
            mask = (mask << 1) | 1

        return n ^ mask
