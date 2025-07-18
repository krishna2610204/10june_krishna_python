"""Practical Example 3: Write a Python program to find a specific string in the list using a simple
for loop and if condition."""


list1 = ['apple', 'banana', 'mango', 'grapes', 'orange']

search_fruit = input("Enter the name of the fruit to search: ").lower()

found = False

for fruit in list1:
    if fruit == search_fruit:
        found = True
        break

if found:
    print(f"{search_fruit.capitalize()} is found in the list.")
else:
    print(f"{search_fruit.capitalize()} is not in the list.")