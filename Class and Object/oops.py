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

# class Car:
#     # color = "Black"
#     @staticmethod
#     def  start_engine():
#         return "Engine started"
#     @staticmethod
#     def  stop_engine():
#         return "Engine stopped"
    
# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type


# car1 = Fortuner("Diesel")
# print(car1.start_engine())

# car1 =  ToyotaCar("Fortuner")
# car2 = ToyotaCar("Corola")

# print(car1.name)
# print(car1.start_engine())
# print(car2.name)
# print(car2.start_engine())
# print(car1.color)

# Types of Inheritence in Python:
# 1. Single Inheritance: In single inheritance, a child class inherits the properties and methods  of a single parent class(base class).
# class Car:
#     # color = "Black"
#     @staticmethod
#     def  start_engine():
#         return "Engine started"
#     @staticmethod
#     def  stop_engine():
#         return "Engine stopped"
    
# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("Diesel")
# print(car1.start_engine())

# car1 =  ToyotaCar("Fortuner")
# car2 = ToyotaCar("Corola")

# print(car1.name)
# print(car1.start_engine())
# print(car2.name)
# print(car2.start_engine())
# print(car1.color)
# 2. Multiple Inheritance: In multiple inheritance, a child class inherits the properties and methods of more than one parent class.

# class A:
#     varA =  "Welcome to Class A"

# class B:
#     varB = "Welcome to Class B"

# class C(A, B): #  C is child class and A and B are parent classes
#     varC =  "Welcome to Class C"

# c1 =  C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)


# Super method:  The super() function in Python is used to give access to methods and properties of a parent or sibling  class. It returns a proxy object that allows you to call methods of its parent class.  It is used to invoke methods of a superclass from a subclass.

# class Car:

#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def  start_engine():
#         print("Engine started...")
#     @staticmethod
#     def  stop_engine():
#         print("Engine Stopped...")
    
# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start_engine()
        
# car1 = ToyotaCar("Urban Cruiser", "electric")
# print(car1.type)

# Class method: A class method is a method that is called on a class rather than on an instance of the  class. It is used to create a new instance of the class. It is used to create a  new instance of the class.

# class Person:
#     name = "anonymous"
    
#     # def changeName(self, name):
#     #     self.__class__.name = name # self.__class__ is used to access the class itself
#     #     # Person.name = name #  class method  to change the class variable
#     @classmethod
#     def changeName(cls, name):
#         cls.name = "John" # class method to change the class variable

# p1 =  Person()
# print(p1.name)
# p1.changeName("Kunal Choudhary")
# print(p1.name)
# print(Person.name)

# Instance Methods: Use self to access and modify the instance.

# Class Methods: Use cls to access and modify the class.

# Static Methods: Don’t access instance or class data; standalone functions within the class.

# @property Decorator:  This is a read-only property. It can be used to make a method look like an attribute.

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy +  self.chem + self.math) / 3) + "%"

#     def calculatePercentage(self):
#        self.percentage = str((self.phy +  self.chem + self.math) / 3) + "%" 

#     @property # decorator to make a method look like an attribute
#     def percentage(self):  # read-only property
#         return  str((self.phy +  self.chem + self.math) / 3) + "%"
 
# s1 =  Student(99,91,93)
# print(s1.percentage)

# s1.phy = 100
# print(s1.phy)
# s1.calculatePercentage()
# print(s1.percentage)

# s1.phy = 85
# print(s1.percentage)


# 3. Multilevel Inheritance: In multilevel inheritance, a child class inherits  the properties and methods  of a parent class, and the parent class also inherits the properties and methods of another parent class.

# class  GrandParent:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print("GrandParent name:", self.name, "age:", self.age)


# class Parent(GrandParent):
#     def __init__(self, name, age, address):
#         super().__init__(name, age)
#         self.address = address
#     def display(self):
#         super().display()
#         print("Parent name:", self.name, "age:", self.age, "address:", self.address )


# class Child(Parent):
#     def __init__(self, name, age, address, grade):
#         super().__init__(name, age, address)
#         self.grade = grade
#     def display(self):
#         super().display()
#         print("Child name:", self.name, "age:", self.age, "address:", self.address , "grade:", self.grade)

# g1 = GrandParent("Rahul", 25)
# g1.display()
# print(g1.name, g1.age)


# Polymorphism: Operator overloading
# when the same operator is used with different operands and different operations are performed, it is called operator overloading.

# print(1 + 2) # 3
# print("Hello" + "World") # operator overloading
# print([1,2,3] + [4,5,6]) # merge



# Polymorphism is the ability of an object to take on multiple forms. This can be achieved through method overriding or method overloading.
# Method Overriding: When a subclass provides a different implementation of a method that is already available in its superclass, it is known as method overriding.  The method in the subclass has the same name, same parameters, but different implementation.
# Method Overloading: When two or more methods in a class have the same name but different  parameters, it is known as method overloading.The method to be invoked is determined at compile time.It is not possible in Python.

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def  showNumber(self):
#         print(self.real,"i+", self.img,"j")

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal,  newImg)
    
#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal,  newImg)
    
#     def __mul__(self, num2):
#         newReal = self.real * num2.real - self.img * num2.img
#         newImg = self.real * num2.img + self.img * num2.real
#         return Complex(newReal,  newImg)
#     def  __truediv__(self, num2):
#         newReal = (self.real * num2.real + self.img * num2.img) / (num2.real ** 2 + num2.img ** 2)
#         newImg = (self.img * num2.real - self.real * num2.img) / (num2.real ** 2 + num2.img ** 2)
#         return Complex(newReal,  newImg)

# num1 =  Complex(3, 4)
# num1.showNumber()

# num2 =  Complex(9, 7)
# num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()

# num3 = num1 + num2
# num3.showNumber()



# Let's Practice with the following problem:

#Qs. Define a circle class to create a circle with radius using the constructor.
# Define a Area()  method to calculate the area of the circle.
# Define a perimeter() method  to calculate the perimeter of the circle.

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return (22/7) * (self.radius ** 2)
#     def perimeter(self):
#         return 2 * (22/7) * self.radius

# c1 =  Circle(21)

# print(c1.area()) # Output: 1380.84
# print(c1.perimeter()) # Output: 132.0


# Qs. Define a Employee class with attributes role, department & salary. This class should also contain a showDetails() method.
# Create a Engineer class  that inherits from Employee & has additional attributes  like experience & skills.


# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
#     def showDetails(self):
#         print(f"Role: {self.role}")
#         print(f"Department: {self.department}")
#         print(f"Salary: {self.salary}")

# class Engineer(Employee):
#     def __init__(self, role, department, salary, experience, skills):
#         super().__init__(role, department, salary)
#         self.experience = experience
#         self.skills = skills
#         self.showDetails()
#     def  showDetails(self):
#         super().showDetails()
#         print(f"Experience: {self.experience}")
#         print(f"Skills: {self.skills}")

# # Creating an  object of Employee class
# emp1 = Employee("Software Engineer", "IT", 50000)
# emp1.showDetails()
# print("EMP2")
# # Creating an object of Engineer class
# emp2 =  Engineer("Software Engineer", "IT", 50000, 5, ["Python", "Java"])
# emp2.showDetails()


# #Qs. Create a class called Order which stores item & its price. Use Dunder function __gt__() to convey that

# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price
#     def  __gt__(self, other):
#         return self.price > other.price

# # Creating objects of Order class
# order1 = Order("Apple", 10)
# order2 = Order("Banana", 5)
# # Comparing two objects using > operator
# print(order1 > order2)  # Output: True










