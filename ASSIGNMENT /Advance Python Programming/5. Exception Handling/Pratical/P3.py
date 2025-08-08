"""Write a Python program to handle file exceptions and use the finally block for closing
the file"""

try:
    file = open("test.txt", "r")   # Try to open file
    data = file.read()
    print(data)

except FileNotFoundError:
    print("File not found!")

finally:
    try:
        file.close()   # Close file if it was opened
        print("File closed.")
    except NameError:
        print("No file to close.")
