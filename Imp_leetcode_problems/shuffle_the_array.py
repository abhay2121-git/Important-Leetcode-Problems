# Example 1:

# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0] * (2 * n)
        j = 0
        for i in range(n):
            res[j] = nums[i]
            res[j + 1] = nums[i + n]
            j += 2
        return res