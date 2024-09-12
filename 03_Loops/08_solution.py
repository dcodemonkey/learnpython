number = int(input("Enter a number check the entered number is prime or not: "))
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
if is_prime == True:
    print(number, " is a Prime number.")
else:
    print(number, " is not a prime number.")