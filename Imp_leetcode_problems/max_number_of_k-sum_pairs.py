# Example 1:
# Input: nums = [1,2,3,4], k = 5
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1

from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        operations = 0

        while l < r:
            current_sum = nums[l] + nums[r]

            if current_sum == k:
                operations += 1
                l += 1
                r -= 1

            elif current_sum < k:
                l += 1

            else:
                r -= 1
            
        return operations
