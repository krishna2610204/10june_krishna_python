"""Write Python programs to demonstrate different types of inheritance (single, multiple,
multilevel, etc.)."""

# Single Inheritance Example
class Animal:
    def speak(self):
        print("Animals make sounds.")

class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof Woof!")

d = Dog()
d.speak()  
d.bark()  


# Multiple Inheritance Example
class Father:
    def skill(self):
        print("Father: Knows gardening.")

class Mother:
    def hobby(self):
        print("Mother: Loves painting.")

class Child(Father, Mother):
    def talent(self):
        print("Child: Good at music.")

c = Child()
c.skill()   
c.hobby()  
c.talent() 


# Multilevel Inheritance Example
class Grandparent:
    def wisdom(self):
        print("Grandparent: Shares life lessons.")

class Parent(Grandparent):
    def guidance(self):
        print("Parent: Gives guidance.")

class Child(Parent):
    def learn(self):
        print("Child: Learning from parents and grandparents.")

c = Child()
c.wisdom()  
c.guidance()
c.learn()  

# Hierarchical Inheritance Example
class Vehicle:
    def fuel_type(self):
        print("Vehicle uses fuel.")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels.")

class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels.")

car = Car()
bike = Bike()

car.fuel_type()
car.wheels()

bike.fuel_type()
bike.wheels()


# Hybrid Inheritance Example
class Person:
    def info(self):
        print("I am a person.")

class Student(Person):
    def study(self):
        print("I am studying.")

class Worker(Person):
    def work(self):
        print("I am working.")

class Intern(Student, Worker):  # Multiple + Hierarchical
    def role(self):
        print("I am an intern.")

# Create object of Intern
i = Intern()
i.info()  
i.study()
i.work()  
i.role()  
