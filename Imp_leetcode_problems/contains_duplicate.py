class Solution:
    def contains_duplicates(self, nums):
        a = set()
        for num in nums:
            if num in a:
                return True
            else:
                a.add(num)
        return False
