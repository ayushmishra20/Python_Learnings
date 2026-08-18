'''# Inheritance in python
When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.
## Python Inheritance Syntax
```python
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
  ```
Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.
## Types of inheritance:
1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance

We will see the explaination and example of each type of inheritance in the later tutorials
'''



class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"employee id{self.id} & name is {self.name}")
        
    
class programmer(employee):
    def showLanguage(self):
        print("default language is python")
        
e1 = employee("Rohan, 20")
e1.showDetails()
e2 = programmer("Ashish", 302)
e2.showDetails()