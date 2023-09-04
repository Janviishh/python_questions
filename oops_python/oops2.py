# class Customer:
#     def __init__(self,name,gender) -> None:
#         self.name=name
#         self.gender=gender
# def greet(customer):
#     if customer.gender=="Male":
#         print("Hello",customer.name,"sir")
#     else:
#         print("Hello",customer.name,"ma'am")
# cust=Customer("Janvi","female")
# greet(cust)
import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# Example usage
rectangle = Rectangle(5, 10)
circle = Circle(3)

print("Rectangle Area:", rectangle.area())
print("Circle Area:", circle.area())
