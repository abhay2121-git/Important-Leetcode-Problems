# Jewels and stones
# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# output : 3

# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0


class Solution:
    def jewels_stones(self, stones, jewels):
        c = 0
        for s in stones:
            if s in jewels:
                c += 1
        return c
