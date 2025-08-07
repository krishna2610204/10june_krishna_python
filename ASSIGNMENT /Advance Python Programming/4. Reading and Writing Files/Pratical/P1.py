"""Write a Python program to create a file and print the string into the
file. """

text = "my name is krishna"

with open('file.txt' , 'w') as file:
    file.write(text)

text.close()


