"""Write a Python program to create a file and write a string into it."""

text = input("Enter string into it: ")

with open("Text1.txt", 'w') as file:
    file.write(text)

print("Text written successfully.")
