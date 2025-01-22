import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height    
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):    
        return 2 * (self.width + self.height)
    
    def diagonal_length(self):
        return math.sqrt(self.width**2 + self.height**2)
 
x = int(input("Enter the width: "))
y = int(input("Enter the height: "))
a = Rectangle(x, y)
print(a.area())
print(a.perimeter())
print(a.diagonal_length())
