"""Write a Python program to check the current position of the file cursor using tell()."""

file = open("Text1.txt", "r")


data = file.read() 

position = file.tell()
print(f"Current cursor position: {position}")

file.close()
