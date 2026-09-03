
class String:
    def rotate_string(self, s, goal):
        if len(s) != len(goal):
            return False
        
        c = s + s
        return goal in c
s = "oomb"
goal = "boom"
result = String(s, goal).rotate_string()
print(result)
