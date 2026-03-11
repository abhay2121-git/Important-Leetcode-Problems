# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
