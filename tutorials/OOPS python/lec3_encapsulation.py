class publicExample:
    def __init__(self,name):
        self.name = name
    def display (self):
        print("Hello i am public variable", self.name)

object = publicExample("paritosh")
print(object.name)
object.display()

class protectedExample:
    def __init__(self,name):
        self._name = name
    def display(self):
        print("Hello i am protected variable", self._name)

object2 = protectedExample("arnav")
print(object2._name)
object2.display()


class privateExample():
    def __init__(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name

object3 = privateExample("arya")
print(object3.get_name())  # Output: Charlie
object3.set_name("Dave")
print(object3.get_name()) 
