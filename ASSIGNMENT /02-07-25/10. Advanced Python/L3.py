"""Write a Python program that filters out even numbers using the filter() function."""

List1 = [2,4,5,6,7,8,90]
a = filter(lambda a : a%2 ==0 , List1)
print(list(a))