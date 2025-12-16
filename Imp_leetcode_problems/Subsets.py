# Subsets
# Example 1:
# Input: nums = [1, 2, 3]
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# Example 2:
# Input: nums = [0]
# Output: [[], [0]]

class Solution:
    def __init__(self, nums):
        self.nums = nums

    def subsets(self):
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            # Don't pick nums[i]
            backtrack(i + 1)

            # Pick nums[i]
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)
        return res

nums = [1, 2, 3]
sol = Solution(nums).subsets()
print(sol)