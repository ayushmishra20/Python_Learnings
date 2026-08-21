# Class Methods as Alternative Constructors
'''
In object-oriented programming, the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class. The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use.

However, there are times when you may want to create an object in a different way, or with different initial values, than what is provided by the default constructor. This is where class methods can be used as alternative constructors.

A class method belongs to the class rather than to an instance of the class. One common use case for class methods as alternative constructors is when you want to create an object from data that is stored in a different format, such as a string or a dictionary. For example, consider a class named "Person" that has two attributes: "name" and "age". The default constructor for the class might look like this:


But what if you want to create a Person object from a string that contains the person's name and age, separated by a comma? You can define a class method named "from_string" to do this:


Another common use case for class methods as alternative constructors is when you want to create an object with a different set of default values than what is provided by the default constructor. For example, consider a class named "Rectangle" that has two attributes: "width" and "height". The default constructor for the class might look like this:
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

```
But what if you want to create a Rectangle object with a default width of 10 and a default height of 5? You can define a class method named "square" to do this:
```python
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  @classmethod
  def square(cls, size):
    return cls(size, size)
```
Now you can create a square rectangle like this:

```python
rectangle = Rectangle.square(10)
```
## [Next Lesson>>](https://replit.com/@codewithharry/71-Day-71-dir-dict-and-help-methods)
'''


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
    
    
e1 = Employee("Harry", 60000)
print(e1.name)
print(e1.salary)

String = "Jhon-12000"

e2 = Employee.fromstr(String)
print(e2.name)
print(e2.salary)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def from_String(cls, String):
        name, age = String.split(',')
        return cls(name, int(age))
    
person = Person.from_String(("John Doe, 30"))
print(person.name, person.age)
