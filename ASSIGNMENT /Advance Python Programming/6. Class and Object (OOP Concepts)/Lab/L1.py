"""Write a Python program to create a class and access its properties using an object."""

class info:
    name = input("Enter name:")
    age = int(input("Enter age:"))
    gender = input("Male/Female:")

information = info()

print("\n--- User Information ---")
print("Name:", information.name)
print("Age:", information.age)
print("Gender:", information.gender)

