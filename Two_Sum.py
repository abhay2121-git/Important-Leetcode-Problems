class TwoSum:
    def __init__(self, nums):
        self.nums =  nums
    
    def two_sum(self):
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]    # {3, 5, 7, 4, 6, 9}
            hashmap[num] = i
nums = [3, 5, 7, 4, 6, 9]
target = 8
two_summ = TwoSum(nums).two_sum()
print(two_summ)



# nums = [2, 4, 5, 8, 9, 7]
# target = 6

class Solution:
    def __init__(self, nums):
        self.nums = nums

    def twoo_summ(self):
        hashmp = {}
        for i, num in enumerate(nums):
            difff = targett - num
            if difff in hashmp:
                return [hashmp[difff], i]
            hashmp[num] = i

nums = [2, 4, 5, 8, 9, 7]
targett = 10
ans = Solution(nums).twoo_summ()
print(ans)