"""Write a Python program to search for a word in a string using
re.search()."""

import re

text = "I love swimming in the ocean"
word = "swimming"

match = re.search(word, text)

if match:
    print(f"'{word}' found at position {match.start()} to {match.end()}")
else:
    print(f"'{word}' not found in the string.")
