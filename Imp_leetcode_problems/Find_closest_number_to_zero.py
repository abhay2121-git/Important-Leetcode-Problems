# Number closest to zero
# Example 2
# Input : nums = [-4, -2, 1, 4, 8]
# Output : 1

# Example 2
# Input : nums = [2, -1, 1] 
# Outpt : 1

class Solution:
    def __init__(self):
        pass

    def findclosestnumber(self, nums):
        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
            
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest

nums = [-4, -2, 1, 4, 8]
sol = Solution().findclosestnumber(nums)
print(sol)