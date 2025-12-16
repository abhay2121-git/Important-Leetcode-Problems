# Square of a sorted array
# Example 1:
# Input: nums = [-4, -1, 0, 3, 10]
# Output = [0, 1, 9, 16, 100]

# Example 2:
# Input : nums = [-7, -3, 2, 3, 11]
# Output: [4, 9, 9, 49, 121]

class Sorted:
    def __init__(self, nums):
        self.nums = nums

    def sortedd_square(self):
        n = len(nums)
        L, R = 0, n - 1
        res = [0] * n

        for i in range(n - 1, -1, -1):
            if abs(nums[L]) > abs(nums[R]):
                val = nums[L]
                L += 1
            else:
                val = nums[R]
                R -= 1
            res[i] = val ** 2
        return res
nums = [-4, -1, 0, 3, 10]
print(Sorted(nums).sortedd_square())


# Another method to solve it
# But it performs less as compare to first one.
class Solution:
    def __init__(self, nums):
        self.nums = nums

    def sorted_squares(self):
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1
        result.reverse()
        return result
    
nums = [-4, -1, 0, 3, 10]
print(Solution(nums).sorted_squares())

