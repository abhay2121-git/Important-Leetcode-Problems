# Example 1:
# Input : num = 16
# Output : true

# Example 2:
# Input : num = 14
# Output = false


class Solution:
    def __init__(self, num):
        self.num = num

    def valid_perfect_square(self):
        l = 1
        r = num

        while l <= r:
            mid = (l + r) // 2
            mid_sqaured = mid * mid

            if num == mid_sqaured:
                return True
            
            elif num > mid_sqaured:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return False

num = 16
print(Solution(num).valid_perfect_square())

