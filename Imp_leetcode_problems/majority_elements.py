# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
#  You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


class SOlution:
    def __init__(self):
        pass

    def majority_ele(self, nums):
        ans = -1
        count = 0

        for num in nums:
            if count == 0:
                ans = num
            
            if ans == num:
                count += 1
            else:
                count -= 1
        
        return ans

nums = [2,2,1,1,1,2,2]
print(SOlution().majority_ele(nums))


class Sol:
    def __init__(self):
        pass

    def majority_elementss(self, nums):
        ans = -1
        count = 0

        for num in nums:
            if count == 0:
                ans = num
            
            if ans == num:
                count += 1
            else:
                count -= 1
        
        return ans

nums = [2, 3, 4, 1, 5, 6, 3]
print(Sol().majority_elementss(nums))