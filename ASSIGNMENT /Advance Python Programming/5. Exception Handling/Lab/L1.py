"""Write a Python program to handle exceptions in a simple calculator (division by zero, invalid
input)."""

a = int(input("Enter Number:"))
b = int(input("Enter Number:"))

add = a + b 
print("Addition of is :",add)

sub = a - b
print("Subtraction is :",sub)

multi = a * b
print("Multiplication is:",multi)

try :
    div = a/b
    print("Division is :",div)

except (ZeroDivisionError) :
    print("Error : cannot divide by zero")




