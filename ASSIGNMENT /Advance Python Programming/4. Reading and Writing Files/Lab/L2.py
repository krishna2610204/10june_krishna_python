"""Write a Python program to write multiple strings into a file."""

with open("file.txt", "w") as file:
    print("Enter multiple lines (type 'STOP' to end):")
    while True:
        line = input()
        if line.upper() == 'STOP':
            break
        file.write(line + '\n')



