""" Write a Python program to show single inheritance."""

class Animal:
    def speak(self):
        print("Animals make sounds.")

class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof Woof!")

d = Dog()
d.speak()  