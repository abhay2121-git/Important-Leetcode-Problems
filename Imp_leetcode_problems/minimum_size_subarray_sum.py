# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        min_len = float('inf')
        cur_sum = 0

        for right in range(n):
            cur_sum += nums[right]

            while cur_sum >= target:
                min_len = min(min_len, right - left + 1)

                cur_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0