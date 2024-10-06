# number = int(input("Enter a number to get qube: "))

# def cube(num):
#     return num ** 3

# result = cube(number)
# print(result)

# number = int(input("Enter a number to get prime: "))

# def prime(number):
#     for i in range(2, number): #2 #3
#         print(i)
#         if number % i == 0: # 5%2 == 0 5%3 == 0 5%4 == 0
#             return False
#     return True
        
        

# print(prime(number))     

# number = int(input("Enter a number:"))

# def factorial(number):
#     result = 1 # 1
#     for i in range(1, number+1): #1 #4 #3 #2 #1
#         print(i)
#         result *= i #1*5 #2*5# #3*10 #4*30
#     return result
    
# print(factorial(5))


### ouput = {"even":[2,4,6,8,...], "odd":[1,3,5,7 ...]}
number = 100


def oddeven(number):
    d = {'even': [], 'odd': []}
    for i in range(number):
        if i % 2 == 0:
            d.get('even').append(i)
        else:
            d.get('odd').append(i)
    return d

print(oddeven(number))

    
 

