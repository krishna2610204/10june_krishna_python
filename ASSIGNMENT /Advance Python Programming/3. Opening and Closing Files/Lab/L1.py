"""Write a Python program to open a file in write mode, write some text, and then close it."""

file1 = open("Intro.txt" , 'w')

file1.write("Hello! This is an intro text file.\nWelcome to file handling in Python.")

file1.close()