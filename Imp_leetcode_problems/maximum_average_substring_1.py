# Maximum average substring 1

# Example 1: 
# Input : nums = [1, 12, -5, -6, 50, 3], k = 4
# Output : 12.75000
# Explanation : Maximum average is (12-5-6+50) / k

class Solution:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k

    def maximum_average_substring(self):
        n = len(nums)
        cur_sum = 0

        for i in range(k):
            cur_sum += nums[i]

        max_avg = cur_sum / k

        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i - k]

            avg = cur_sum / k

            max_avg = max(max_avg, avg)
        return max_avg
    
nums = [1, 12, -5, -6, 50, 3]
k = 4
maxx = Solution(nums, k).maximum_average_substring()
print(maxx)