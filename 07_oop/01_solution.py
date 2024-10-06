class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Deisel"
    
    @staticmethod
    def general_description():
        return "Cars are mean of transport"
    
    @property
    def model(self):
        return self.__model

# Creating ElectricCar class and inheriting the Parent Car properties
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric charge"

# my_NexonEv = ElectricCar("Tata", "Nexon", "40kWh")
# Checking whether the my_NexonEv is instance of Car and ElectricCar class or not.
# print(isinstance(my_NexonEv, Car))
# print(isinstance(my_NexonEv, ElectricCar))


# print(my_NexonEv.__brand)
# print(my_NexonEv.fuel_type())

# safari = Car("Tata", "Safari")
# print(safari.fuel_type())
# print(safari.total_car)

# my_car = Car("Tata", "Safari")
# my_car.model = "City"
# print(Car.general_description())
# print(my_car.model)



# print(my_NexonEv.brand)
# print(my_NexonEv.get_brand())


# my_Car = Car("Toyota", "Corolla")
# print(my_Car.brand)
# print(my_Car.model)
# print(my_Car.full_name())

# my_new_car = Car("Tata", "Harrier")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())


class Engine:
    def engine_info(self, horse_power):
        self.hp = horse_power
        return f"This engine information: {self.hp}"

class Battery:
    def battery_info(self, watt_hours):
        self.watt_hours = watt_hours
        return f"This is battery information: {self.watt_hours}"

class ElectricEv(Car, Engine, Battery):
    pass

my_new_byd = ElectricEv("BYD", "Big Boys Toys")
print(my_new_byd.model)
print(my_new_byd.engine_info(1))
print(my_new_byd.battery_info(17))






