"""Write a Python program to show hybrid inheritance. """

class person:
    def info(self):
        print("I am person")

class student(person):
    def study(self):
        print("I am studing")

class worker(person):
    def work(self):
        print("I am working")

class Intern(student,workerorker):  # Multiple + Hierarchical
    def role(self):
        print("I am an intern.")


i = Intern()
i.info()   # from Person
i.study()  # from Student
i.work()   # from Worker
i.role()