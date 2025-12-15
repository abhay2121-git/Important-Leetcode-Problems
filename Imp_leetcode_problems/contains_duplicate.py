# class Solution:
#     def __init__(self, nums):
#         self.nums = nums

#     def contains_duplicates(self):
#         a = set()
#         for num in nums:
#             if num in a:
#                 return True
#             else:
#                 a.add(num)
#         return False
# nums = [1, 2, 4, 8, 3, 8, 7]
# print(Solution(nums).contains_duplicates())


class Sol:
    def __init__(self):
        pass

    def contains_duplicates(self, nums):
        a = set()
        for num in nums:
            if num in a:
                return True
            else:
                a.add(num)
        return False

nums = [1, 2, 3, 4]
print(Sol().contains_duplicates(nums))