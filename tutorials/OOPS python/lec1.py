class student:

    college = "ABC college"

    def __init__(self,fullname):
        self.name = fullname
        print(self.name ," student is created!!")
    
    @staticmethod #decorator 
    def hello():
        print("Hello!!")

    def __del__(self):
        print(self.name ," student is deleted!!")

    
s = student("paritosh")
s.hello()
print(student.college) #accessing class variable
del s