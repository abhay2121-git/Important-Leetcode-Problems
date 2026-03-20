# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2

# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2

from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        curr_end = 0
        farthest = 0

        for i in range(n):
            farthest = max(farthest, i + nums[i])

            if i == curr_end:
                jumps += 1
                curr_end = farthest

            if curr_end == n - 1:
                break
        
        return jumps