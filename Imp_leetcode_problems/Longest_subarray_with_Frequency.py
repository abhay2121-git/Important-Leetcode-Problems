# Hackerrank Question
# Given an array of integers, what is the lenght of the longest subarray containing no more than two distinct values
# such that the distinct values differ by no more than 1? 
# Example : arr = [0, 1, 2, 1, 2, 3], the largest such subarray has length : 4[1, 2, 1, 2].
#         : arr = [1, 1, 1, 3, 3, 2, 2], the largest such subarray has lenght : 4[3, 3, 2, 2]

# Sample Case:
# arr = [5, 1, 2, 3, 4, 5]
# Sample Output : 2

from collections import defaultdict

class Solution:
    def __init__(self):
        pass
    
    def longest_subarray(self, arr):
        count = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(arr)):
            count[arr[right]] += 1

            while len(count) > 2 or (len(count) == 2 and abs(max(count) - min(count)) > 1):
                count[arr[left]] -= 1
                if count[arr[left]] == 0:
                    del count[arr[left]]
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len

arr = [5, 1, 2, 1, 2, 5]
sol = Solution().longest_subarray(arr)
print(sol)