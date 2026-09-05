# Input: arr[] = [1, 2, 3, 4, 5], k = 3
# Output: [3, 2, 1, 5, 4]
# Explanation: First group consists of elements 1, 2, 3. Second group consists of 4, 5.
# Input: arr[] = [5, 6, 8, 9], k = 5
# Output: [9, 8, 6, 5]
# Explnation: Since k is greater than the number of remaining elements, the entire array is reversed.

class Solution:
    def reverseInGroups(self, arr, k):

        n = len(arr)

        for i in range(0, n, k):
            left = i
            right = min(i + k - 1, n - 1)

            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        return arr