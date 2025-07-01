"""Write a Python program that uses a custom iterator to iterate over a list of integers."""

class MyIterator:
    def __init__(self, data):
        self.data = data       
        self.index = 0         

    def __iter__(self):
        return self           

    def __next__(self):
        if self.index < len(self.data):      
            result = self.data[self.index]   
            self.index += 1                 
            return result                    
        else:
            raise StopIteration             



numbers = [5, 10, 15, 20]


my_iter = MyIterator(numbers)


for number in my_iter:
    print(number)
