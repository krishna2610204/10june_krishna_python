"""Write a Python program to show hierarchical inheritance."""

class Shapes:
    def shapes(self):
        print("There are many shapes")

class circle(Shapes):
    def Circle(self):
        print("Circle has no sides")

class square(Shapes):
    def Square(self):
        print("Square has 4 sides")

class triangle(Shapes):
    def triangle(self):
        print("Triangle has 3 sides")

c = circle()
s = square()
t = triangle()


c.shapes()
c.Circle()

s.shapes()
s.Square()

t.shapes()
t.triangle()