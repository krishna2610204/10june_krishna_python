"""Write a Python program to show method overriding."""

class Animal:
    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):
    def sound(self):
        print("Dog barks: Woof Woof!")

a = Animal()
d = Dog()

a.sound() 
d.sound()