"""Write a Python program to show method overloading."""

class AreaCalculator:
    def area(self, length=0, width=0):
        if length != 0 and width != 0:
            print("Area of rectangle:", length * width)
        elif length != 0:
            print("Area of square:", length * length)
        else:
            print("No dimensions given.")

calc = AreaCalculator()

calc.area(5, 10) 
calc.area(7)     
calc.area()    