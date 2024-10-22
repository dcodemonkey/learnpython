# OOPS in Python - To map with real world scanarios, we started using the  concept of classes and objects in code.

# 1. Classes, Objects and Constructors
# Classes are like blueprints or templates for creating objects. Objects are instances of classes.
# We can create multiple objects from a single class.
# Classes are defined using the class keyword.
# class Car:
    # This is a class variable, it is shared by all instances of the class
    # wheels = 4 # This is a class variable
    # This is a method, it is a function that belongs to the class
    # def __init__(self, brand, model, year):
        # This is a constructor method, it is called when an object is created from the class
        # self is a reference to the current instance of the class and is used to access variables and methods from the class.
    #     self.brand = brand
    #     self.model = model
    #     self.year = year
    # def describe_car(self):
        # This is a method that belongs to the class
        # print(f"This car is a {self.year} {self.brand} {self.model}")
# Now we can create objects from the class
# my_car  = Car("Toyota", "Camry", 2020)
# We can access the class variables and methods using the object
# print(my_car.wheels)  # Output: 4
# print(my_car.brand)   # Output: Toyota
# print(my_car.model)   # Output: Camry
# print(my_car.year)    # Output: 2020
# We can call the methods using the object
# my_car.describe_car()  # Output: This car is a 2020 Toyota Camry

# class Student:
#     def __init__(self, name, age, marks, grade):
#         self.nam = name
#         self.umar = age
#         self.scores = marks
#         self.grade =  grade

#     def welcome(self):
#         print(f"Hello, my name is {self.nam} and I am {self.umar} year old, my current grade is {self.grade}")

#     def average(self):
#         grd = 0
#         for i in  self.scores:
#             grd += i
#         print(f"Hi, {self.nam}  your average is {grd/len(self.scores)}")

   
# s1 = Student("Kunal", 27, [99,89,97])
# print(s1.nam) # Output: Kunal
# print(s1.welcome()) #Output: Hello, my name is Kunal and I am 27 old ...

# s2 = Student("Kunal", 27, [99,89,97], "A+")
# print(s2.nam)
# s2.welcome()
# s2.average() # Output: 95.0

# Static Methods: Methods that belong to the class itself, not to any instance of the class.
# In Python, a static method is defined within a class using the @staticmethod decorator. Unlike instance methods, static methods do not require an instance of the class to be called. They do not have access to the instance (self) or class (cls) variables, making them similar to regular functions but scoped within the class.

# class Math:
#     @staticmethod #  This is a decorator that indicates this method is a static method
#     def add(a, b):
#         return a + b
# # Now we can call the static method using the class name
# print(Math.add(5, 7))  # Output: 12

# Decorator: A decorator is a small function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.
# In Python, a decorator is defined using the @ symbol followed by the name of the decorator function.
# The decorator function takes a function as an argument and returns a new function that "wraps"  the original function.
# The new function produced by the decorator is then called instead of the original function when it's invoked.

# def simple_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before calling the function...")
#         result = func(*args, **kwargs)  # Call the original function
#         print("After calling the function...")
#         return result  # Return the result of the original function
#     return wrapper

# @simple_decorator
# def greet(name):
#     """A simple function that greets a person."""
#     return f"Hello, {name}!"

# # Using the decorated function
# greeting = greet("Alice")
# print(greeting)

# Abstraction:  Abstraction is the concept of showing only the necessary information to the outside world while hiding the internal details.
# Abstraction is a fundamental concept in object-oriented programming (OOP) and is used to promote code reusability, modularity, and maintainability.
# In Python, abstraction is achieved through the use of classes and objects.
# Example:
# class Car:
#     def __init__(self):
#         self.accelarator = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.accelarator = True
#         self.clutch = True
#         print("Car started")
    
#     def stop(self):
#         self.accelarator = False
#         self.clutch = False
#         print("Car stopped")

# car1 = Car()
# car1.start()

# Encapsulation:
# Encapsulation is the concept of bundling data and methods that manipulate that data within a single unit , called a class or object.
# Encapsulation is used to hide the internal details of an object from the outside world and only expose  the necessary information through public methods.
# In Python, encapsulation is achieved through the use of classes and objects.
# Example:
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance
#     # debit method
#     def debit(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             return print(f"Debited ${amount}. Remaining balance is ${self.balance}")
#         else:
#             return print("Insufficient balance")
#     # Credit Method
#     def credit(self,  amount):
#         if amount > 0:
#             self.balance += amount
#             return print(f"Credited ${amount}. Remaining balance is ${self.balance}")
#         else:
#             return print("Invalid amount")

# account = BankAccount("12345", 10000)
# account.debit(500)
# account.credit(1000)



# del keyword:  The del keyword is used to delete an object or a variable in Python.

# class Student:
#   def __init__(self, name):
#     self.name = name

# student1 =  Student("John")

# print(student1.name)
# del student1 #  delete the object
# print(student1.name)

# Private(like) attributes &  methods:  In Python, we can use a single underscore prefix to indicate that a method or attribute is intended to be private, but it's not enforced by the language.

# Conceptual Implementation: Private attributes and methods are intended to be used internally within a class and should not be accessed directly from outside the class.


# class BankAccount:
#     def __init__(self, account_number, account_password):
#         self.account_number = account_number
#         self.__account_password = account_password
       
# # create an instance of the class
# account = BankAccount("12345", "password")
# # access the private attribute directly
# print(account.__account_password)  # This will raise an AttributeError


# class Person:
#     __name = "anonymous"

#     def __hello(self, name):
#         self.__name = name
#         print(f"Hello! {name}")
    
#     def welcome(self):
#         self.__hello("Kunal")
#         print(f"Welcome , {self.__name}")


# p1 =  Person()
# p1.welcome()



# Inheritance: Inheritance is a mechanism in object-oriented programming (OOP) where one class can inherit the  properties and methods of another class. The class that is being inherited from is called the parent or superclass , and the class that is doing the inheriting is called the child or subclass.

class Car:
    @staticmethod
    def  start_engine():
        return "Engine started"
    @staticmethod
    def  stop_engine():
        return "Engine stopped"
    
class ToyotaCar(Car):
    def __init__(self, name) -> None:
        self.name = name


car1 =  ToyotaCar("Fortuner")
car2 = ToyotaCar("Corola")

print(car1.name)
print(car1.start_engine())
print(car2.name)
print(car2.start_engine())

# Types of Inheritence in Python:
# 1. Single Inheritance: In single inheritance, a child class inherits the properties and methods  of a single parent class.
# 2. Multiple Inheritance: In multiple inheritance, a child class inherits the properties and methods of more than one parent class.
# 3. Multilevel Inheritance: In multilevel inheritance, a child class inherits  the properties and methods  of a parent class, and the parent class also inherits the properties and methods of another parent class.

















# Polymorphism






















