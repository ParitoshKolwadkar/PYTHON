class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Animals make sounds"

class Dog(Animal):
    def sound(self):
        return f"{self.name} barks"
    

dog  = Dog("tommy")
print(dog.sound())  # Output: tommy barks

class A:
    def greet (self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"
    
class C(A):
    def greet(self):
        return "Hello from C"

class D(B,C):
    pass

d=D()
print(d.greet())  # Output: Hello from B
print(D.mro())
