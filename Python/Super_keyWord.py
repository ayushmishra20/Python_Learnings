class Employee:
    def __init__(self, name, id):
        self.name = name
        self. id = id
        
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
        
rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "234", "Python") #created Object for Programer

print(harry.name)
print(rohan.name)
