"""Write Python programs to demonstrate method overloading and method overriding."""

#  Method Overloading

class MathOperations:
    def add(self, a=0, b=0, c=0):
        return a + b + c

math_obj = MathOperations()

print("Sum of 2 numbers:", math_obj.add(5, 10))         # a=5, b=10, c=0
print("Sum of 3 numbers:", math_obj.add(5, 10, 15))     # a=5, b=10, c=15
print("Sum of 1 number:", math_obj.add(7))              # a=7, b=0, c=0



# Method Overriding

class Parent:
    def show_message(self):
        print("This is the parent class message.")

class Child(Parent):
    def show_message(self):
        print("This is the child class message.")

p = Parent()
c = Child()

p.show_message()
c.show_message()