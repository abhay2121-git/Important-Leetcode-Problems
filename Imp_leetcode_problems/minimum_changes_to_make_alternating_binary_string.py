# Example 1:
# Input: s = "0100"
# Output: 1

# Example 2:
# Input: s = "10"
# Output: 0

# Example 3:
# Input: s = "1111"
# Output: 2

class Solution:
    def minOperations(self, s: str) -> int:
        operations = 0

        for i, c in enumerate(s):
            if c != str(i % 2):
                operations += 1
        
        return min(operations, len(s) - operations)
    