"""Write a Python program to create a dictionary of 6 key-value pairs."""

ex = {'Peacock' : 'National Bird' ,
      'Tiger' : 'National Animal', 
      'Lotus' : 'National Flower',
      'Jana Gana Mana' : 'National Anthem',
      'Vande Mataram' : 'National Song',
      'Indian Rupee' : 'NAtional Currency'}

for key , value in ex.items():
    print(key, ':' ,value)