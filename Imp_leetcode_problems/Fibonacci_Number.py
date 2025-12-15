# Example 1:
# Input : n = 2
# Output : 1

# Example 2:
# Input : n = 3
# Output : 2

# Top Down DP / Memoization
class Solution:
    def __init__(self):
        self.memo = {0:0, 1:1}

    def f(self, n):
        if n in self.memo:
            return self.memo[n]
        
        else:
            self.memo[n] = self.f(n - 1) + self.f(n - 2)
        
        return self.memo[n]

n = 7
sol = Solution().f(n)
print(sol)

# With Bottom-Up DP 
class Soll:
    def __init__(self, n):
        self.n = n
    
    def fibo(self):
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        prev = 0
        cur = 1

        for i in range(2, n + 1):
            prev, cur = cur, prev + cur

        return cur

n = 6
sool = Soll(n).fibo()
print(sool)