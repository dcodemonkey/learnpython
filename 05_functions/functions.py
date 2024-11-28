# functions in Python:
# 1. Built-in functions: These are functions that are already available in Python. For example, print(), len(), type(), etc

# print("Hello, World!")
# list = [1,2,3,4,5]
# print(len(list))

# print(type(list))

# 2. User-defined functions: These are functions that are created by the user. For example, a function to calculate the area of a circle, etc.

def calculate_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    return area

print(calculate_area(56))


# 3. Lambda functions: These are small anonymous functions that can take any number of arguments, but can only have one expression.

# example of lambda function:
# lambda arguments: expression
# lambda x: x**2
print((lambda x: x**2)(5)) # prints 25

# 4. Anonymous functions: These are functions that are defined without a name.
# example of anonymous function:
# lambda x: x**2
print(lambda x: x**2(5))


# 5. Nested functions: These are functions that are defined inside another function.
# 6. Closure functions: These are functions that have access to their own scope and the scope of their outer functions.
# 7. Decorator functions: These are functions that can modify or extend the behavior of another function.
# 8. Generator functions: These are functions that can be used to generate a sequence of results instead of computing them all at once
# 9. Higher-order functions: These are functions that take other functions as arguments or return functions as output.
