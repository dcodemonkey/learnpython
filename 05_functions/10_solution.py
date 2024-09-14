# def factorial(num):
#     result = 1
#     for i in range(num, 1, -1):
#         result *= i
#         i -= 1
#     return result

# print(factorial(5))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))