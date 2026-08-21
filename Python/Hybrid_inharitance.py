class BAseClass:
    pass

class Derived1(BAseClass):
    pass
class Derived2(BaseClass):
  pass  

class Derived3(Derived1, Derived2):
  pass

# Hierarchical Inheritance
class BaseClass:
  pass

class D1(BaseClass):
  pass

class D2(BaseClass):
  pass

class D3(D1):
  pass