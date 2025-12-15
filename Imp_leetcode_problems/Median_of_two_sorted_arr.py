class Median:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
    
    def median(self):
        nums = nums1 + nums2
        nums = sorted(nums)
        mid = len(nums) // 2

        if len(nums) % 2 != 0:
            return nums[mid]
        
        else:
            mid = nums[mid - 1] + nums[mid]
            return mid / 2.0
nums1 = [1, 2, 3, 4]
nums2 = [5, 6]
numss = Median(nums1, nums2).median()
print(numss)


# nums1 = [1, 2, 3, 4]
# nums2 = [5, 6]
# Output : 3.5


class Solution:
    def __init__(self):
        pass

    def median_of_arrs(self, nums1, nums2):
        nums = nums1 + nums2
        nums = sorted(nums)
        mid = len(nums) // 2

        if len(nums) %2 != 0:
            return nums[mid]
        else:
            mid = nums[mid - 1] + nums[mid]
            return mid/2.0

nums1 = [1, 2, 3]
nums2 = [4]
print(Solution().median_of_arrs(nums1, nums2))