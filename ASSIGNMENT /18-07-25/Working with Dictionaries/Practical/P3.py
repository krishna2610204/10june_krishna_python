"""Write a Python program to convert two lists into one
dictionary using a for loop. """

keys = ['Name', 'Age', 'Course']
values = ['Krishna', 20, 'BCA']

my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i] 
    
print(my_dict)


