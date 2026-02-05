# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = [0,1,1]
# Output: []

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            target = -nums[i]

            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

                elif cur_sum < target:
                    left += 1

                else:
                    right -= 1

        return result