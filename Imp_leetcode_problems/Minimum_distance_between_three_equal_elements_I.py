# Example 1:
# Input: nums = [1,2,1,1,3]
# Output: 6

# Example 2:
# Input: nums = [1,1,2,3,2,1,2]
# Output: 8

# Example 3:
# Input: nums = [1]
# Output: -1

from typing import List
from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)

        for i, val in enumerate(nums):
            pos[val].append(i)

        ans = float('inf')

        for indices in pos.values():
            if len(indices) < 3:
                continue

            for i in range(len(indices) - 2):
                i1 = indices[i]
                i3 = indices[i + 2]

                dist = 2 * (i3 - i1)
                ans = min(ans, dist)

        return ans if ans != float('inf') else -1
    