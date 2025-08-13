"""Write a Python program to search for a word in a string using re.search()."""

import re

text = "Python is a powerful programming language"
word = "powerful"

if re.search(word, text):
    print(f"'{word}' found in the string!")
else:
    print(f"'{word}' not found in the string.")
