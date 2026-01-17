import math
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        gcd = math.gcd(a, b)
        sqrt_gcd = int(math.sqrt(gcd))

        for i in range(1, sqrt_gcd + 1):
            if gcd % i == 0:
                count += 1
                
                if i * i != gcd:
                    count += 1
        
        return count