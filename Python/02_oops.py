class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1

    def get_brand(self):
        return self.__brand

    def Full_Name(self):
        return f"{self.get_brand()}"

    def fuel_type(self):
        return "Petrol Or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are mens for transport"

    @property
    def model(self):
        return self.__model


class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla = Electric_car("Tesla", "S", '85kWh')

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla,Electric_car))

print(my_tesla.get_brand())
print(my_tesla.fuel_type())

mycar = Car('chevi', 'comaro')
print(mycar.Full_Name())

my_car = Car("Tata", "Safari")
# my_car.model = "City"
Car("Tata", "Nexon")



class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())

