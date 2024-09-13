number = int(input('Enter the number to calculate factorial:'))
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1
print("Factorial of given number is:",factorial)