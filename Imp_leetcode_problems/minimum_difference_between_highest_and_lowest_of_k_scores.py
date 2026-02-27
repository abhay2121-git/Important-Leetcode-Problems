# minimum_difference_between_highest_and_lowest_of_k_scores 

# Example 1:
# Input: nums = [90], k = 1
# Output: 0

# Example 2:
# Input: nums = [9,4,1,7], k = 2
# Output: 2

from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = float('inf')
        n = len(nums)

        for i in range(n - k + 1):
            diff = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, diff)

        return min_diff