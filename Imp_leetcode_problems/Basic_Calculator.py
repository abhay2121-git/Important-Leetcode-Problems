# Example 1:
# Input: s = "1 + 1"
# Output: 2

# Example 2:
# Input: s = " 2-1 + 2 "
# Output: 3

# Example 3:
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23

class Solution:
    def calculate(self, s: str) -> int:
        stack  = []
        result = 0
        number = 0
        sign   = 1 

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)

            elif char == '+':
                result += sign * number
                number  = 0
                sign    = 1

            elif char == '-':
                result += sign * number
                number  = 0
                sign    = -1

            elif char == '(':
                stack.append(result) 
                stack.append(sign)
                result = 0 
                sign   = 1

            elif char == ')':
                result += sign * number
                number  = 0
                result *= stack.pop()
                result += stack.pop()

        result += sign * number
        return result
