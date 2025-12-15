class Solution:
    def __init__(self, s, goal):
        self.s = s
        self.goal = goal

    def rotateString(self):
        if len(s) != len(goal):
            return False
        
        c = s + s
        return goal in c

s = "abhay"
goal = "bhaya"
result = Solution(s, goal)
res = result.rotateString()
print(f'Can "{goal}" be obtained by rotating "{s}"?  {res}')


class String:
    def __init__(self, s, goal):
        self.s = s
        self.goal = goal
    
    def rotate_string(self):
        if len(s) != len(goal):
            return False
        
        c = s + s
        return goal in c
s = "oomb"
goal = "boom"
result = String(s, goal).rotate_string()
print(result)
