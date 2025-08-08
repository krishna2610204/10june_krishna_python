"""Write a Python program to demonstrate handling multiple exceptions."""

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    add = a + b
    print("Addition is:", add)

    sub = a - b
    print("Subtraction is:", sub)

    multi = a * b
    print("Multiplication is:", multi)

    div = a / b
    print("Division is:", div)

    file = open("mydata.txt", "r")
    print("File contents:", file.read())
    file.close()

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid integers.")
