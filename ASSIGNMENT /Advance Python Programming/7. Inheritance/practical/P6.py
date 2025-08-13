"""Write a Python program to demonstrate the use of
super() in inheritance."""


class Parent:
    def show_message(self):
        print("This is the parent class message.")

class Child(Parent):
    def show_message(self):
        super().show_message()
        print("This is the child class message.")

c = Child()
c.show_message()
