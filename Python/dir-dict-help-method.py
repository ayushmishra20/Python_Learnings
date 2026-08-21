class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.varsion = 1
        
p = Person("Jhon", 30)
print(p.__dict__)

print(help(Person))