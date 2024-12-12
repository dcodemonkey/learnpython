# class Student:

#     name = "Annonymous"

#     college_name = "Mewar Institute"

#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     @staticmethod # Static method is a method that belongs to a class rather than an instance of a class. it also known as decorator
#     def hello():
#         print("Hello, my name is Python")

# s1 = Student("John", 20, 12)
# print(s1.name, s1.age, s1.grade, s1.college_name)  # Output: John 20 12

# Abstraction

# class Car:
#     __name = "test"
#     nam = "KK"

#     # def __init__(self, make, model, year):
#     #     self.make = make
#     #     self.model = model
#     #     self.year = year

# print(Car) # 
# print(Car.nam) # 

# class Car:
    
#     @staticmethod
#     def start():
#         print("Car started")
#         return "Car started"
    
#     @staticmethod
#     def stop():
#         print("Car stopped")

# class Mahindra(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = Mahindra("XUV")
# car2 = Mahindra("KUV")

# print(car1.name)
# print(car1.start())

# super() method
# class Car:

#     def __init__(self, type):
#         self.type = type
    
#     @staticmethod
#     def start():
#         print("Car started")
#         return "Car started"
    
#     @staticmethod
#     def stop():
#         print("Car stopped")

# class Mahindra(Car):
#     def __init__(self, name, type):
#         super().__init__(type) # calling parent class constructor
#         super().start()
#         self.name = name
        

# # c1 = Car("Electric")
# # print(c1.type)

# c2 = Mahindra("BE600", "Electric")
# print(c2.type)

# Class methods
class Person:
    def __init__(self, name):
        self.name = name



        




