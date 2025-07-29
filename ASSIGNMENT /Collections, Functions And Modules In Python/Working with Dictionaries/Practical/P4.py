"""Write a Python program to count how many times each
character appears in a string."""

x = "My name is Krishna. I am Studing in marwadi university. I have opted BCA. My hobbies are dancing,swimming,badmintion."

count = {}

for ch in x:
    if ch in count:
        count[ch] = count[ch] + 1
    else:
        count[ch] = 1

for ch in count:
    print(ch, ":", count[ch])