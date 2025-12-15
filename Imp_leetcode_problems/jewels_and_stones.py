# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# output : 3

# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0


class Solution:
    def __init__(self, jewels, stones):
        self.jewels = jewels
        self.stones = stones
    
    def jewels_stones(self):
        c = 0
        for s in stones:
            if s in jewels:
                c += 1
        return c
stones = "aAAbbbb"
jewels = "aA"
print(Solution(jewels, stones).jewels_stones())