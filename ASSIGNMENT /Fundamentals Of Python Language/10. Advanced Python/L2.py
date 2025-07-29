"""Write a Python program that uses reduce() to find the product of a list of numbers."""

from functools import reduce

list1 = [23,45,6,7,89,90]
a = reduce (lambda x , y : x * y , list1)
print(a)