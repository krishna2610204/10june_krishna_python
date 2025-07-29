"""Write a Python program to apply the map() function to square a list of numbers."""

list1 = [2,3,4,5,6]
result = map(lambda a : a * a,list1)
print(list(result))