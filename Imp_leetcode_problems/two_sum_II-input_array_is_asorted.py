# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            cur_sum = numbers[left] + numbers[right]

            if cur_sum == target:
                return [left + 1, right + 1]
            
            elif cur_sum < target:
                left += 1
            
            else:
                right -= 1

        return []