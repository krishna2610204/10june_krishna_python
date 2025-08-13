"""Write a Python program to match a word in a string using re.match()."""

import re

text = "Python is a powerful programming language"
word = "Python"

if re.match(word, text):
    print(f"'{word}' is at the start of the string!")
else:
    print(f"'{word}' is NOT at the start of the string.")
