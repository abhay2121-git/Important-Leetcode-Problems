# Example 1:

# Input: n = 5
# Output: 12
# Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7 
        prime_count = self.countPrimesSieve(n)
        non_prime_count = n - prime_count
        return (self.factorial(prime_count, MOD) * self.factorial(non_prime_count, MOD)) % MOD
        
    def countPrimesSieve(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        p = 2
        while p * p <= n:
            if is_prime[p]:
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False
            p += 1
        
        return sum(is_prime)    
    
    def factorial(self, num: int, mod: int) -> int:
        result = 1
        for i in range(2, num + 1):
            result = (result * i) % mod
        return result