"""
Decorator: A function that takes another function as an argument and extends its behavior without explicitly modifying it.
Decorators are often used to add functionality to existing functions or methods in a clean and readable way.
In Python, decorators are often used to modify the behavior of functions or methods.
They are defined using the `@decorator_name` syntax above the function definition.
"""

# import time

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end-start} seconds")
#         return result
#     return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)

# example_function(2)

# Decorators can also be used to modify the behavior of classes and methods.
import time
class Timer:
    """A decorator class that measures the time taken to execute a function."""
    def __init__(self, func):
        self.func = func
    
    def __call__(self, n): 
        """This method is called when the decorated function is called. It measures the time taken to execute the function and prints it."""
        start = time.time() # record the start time
        result = self.func(n) # call the original function
        end = time.time() # record the end time
        print(f"{self.func.__name__} ran in {end-start:.2f} seconds")  # format the time to 2 decimal places
        return result
@Timer
def example_function(n):
    time.sleep(n)
example_function(2)



