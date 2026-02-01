# Example 1:
# Input: nums = [1,2,3,12]
# Output: 6

# Example 2:
# Input: nums = [5,4,3]
# Output: 12

# Example 3:
# Input: nums = [10,3,1,1]
# Output: 12


from typing import List
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        min_additional_cost = float('inf')

        for i in range(1, n-1):
            for j in range(i+1, n):
                additional_cost = nums[i] + nums[j]
                min_additional_cost = min(min_additional_cost, additional_cost)

        return nums[0] + min_additional_cost