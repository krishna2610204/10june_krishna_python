"""Write a Python program to handle multiple exceptions (e.g., file not found, division by zero)."""

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

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid integers.")

except FileNotFoundError:
    print("your file is not there")