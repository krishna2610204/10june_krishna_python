"""Write a Python program to show multiple
inheritance."""

class coder():
    def Coder(self):
        print("Coder do coding")

class  Designer():
    def designer(self):
        print("Designer design the app")

class FullStack(coder,Designer):
    def fullstackdev(self):
        print("Coder + Designer = Full Stack Developer")

f = FullStack()
f.Coder()
f.designer()
f.fullstackdev()