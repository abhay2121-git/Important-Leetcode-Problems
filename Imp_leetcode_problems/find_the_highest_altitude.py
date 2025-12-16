# Example 1:

# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
# Example 2:

# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

class Solution:
    def largestAltitude(self, gain) -> int:
        max_altitude = 0
        current_altitude = 0

        for g in gain:
            current_altitude += g
            max_altitude = max(max_altitude, current_altitude)
        
        return max_altitude

gain = [-5,1,5,0,-7]
sol = Solution().largestAltitude(gain)
print(sol)