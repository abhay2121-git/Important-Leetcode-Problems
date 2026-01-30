# Example 1:
# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: [1,2,3,4,5]

from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices.copy()
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                result[idx] = prices[idx] - prices[i]
            stack.append(i)
        
        return result