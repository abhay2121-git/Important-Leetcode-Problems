class String:
    def __init__(self, string):
        self.string = string

    def reversed_str(self):
        chars = []
        for i in range(len(self.string) -1, -1, -1):
            chars.append(self.string[i])
        return ''.join(chars)
string = 'abcd'
stringg = String(string).reversed_str()
print(stringg)   # O(n)


# With [::-1]
class Stringg:
    def __init__(self, string):
        self.string = string
    
    def reverse_str(self):
        reversed_string = string[::-1]
        print(reversed_string)

string = "abcdef"
Stringg(string).reverse_str()    # O(n)

# Swapping values
class Sol:
    def __init__(self):
        pass

    def swapping(self, g, h):
        g, h = h, g
        print("g: ",g)
        print("h: ",h)

g = 10
h = 20
Sol().swapping(g, h)
