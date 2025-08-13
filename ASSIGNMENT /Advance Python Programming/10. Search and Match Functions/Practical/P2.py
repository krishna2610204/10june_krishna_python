"""Write a Python program to match a word in a string using re.match()."""

import re

text = "Python is fun to learn"
word = "Python"

match = re.match(word, text)

if match:
    print(f"'{word}' is at the start of the string!")
else:
    print(f"'{word}' is NOT at the start of the string.")
