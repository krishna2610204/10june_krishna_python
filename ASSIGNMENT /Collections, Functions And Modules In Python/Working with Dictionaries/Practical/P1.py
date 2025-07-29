"""Write a Python program to update a value at a particular key in a
dictionary"""

info = {'Name' : 'Krishna' , 
        'Age' : 20 , 
        'College name' : 'MArwadi University' , 
        'Current CGPA' : 8.23 ,
        'Course' : 'BCA',
        'Hobbies' : 'Dancing , Swimming , Badmintion',
        'Current Profession' : 'Student'}

info.update({'Age' : 21})

for key , value in info.items():
    print(key, ":" ,value)