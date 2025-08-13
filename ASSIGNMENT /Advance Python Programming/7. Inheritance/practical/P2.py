"""Write a Python program to show multilevel inheritance."""

class Animal:
    def animal(self):
        print("Animals make sound")

class animal(Animal):
    def Animal(self):
        print("Animal eats food")

class dog(animal):
    def dog(self):
        print("Dog barks, eat food also!")

a = dog()              
a.animal()
a.Animal()
a.dog()