"""Write a Python program to demonstrate the use of local and
global variables in a class."""

pi = 3.14

class Math:
    radius = int(input("Enter value of radius: "))

    def area(self):
        area_of_circle = pi * Math.radius * Math.radius
        print("Area of circle:", area_of_circle)

obj = Math()

obj.area()

print("Value of pi (global variable):", pi)
