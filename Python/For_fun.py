class Props:
    name = "Ayush Mishra"
    
    def __init__(self, x, y):
        return self.x + self.y
    
    def full_name(self, name, id):
        self.name = name
        self.id = id
        
    def mul(self,x, y):
        return self.x * self.y
    
obj1 = Props(4,5)
obj1.full_name("Ayush", 21)