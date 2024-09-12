age = int(input('Enter the age know your ticket price: '))
day = input("Enter the day name for discount: ")
price = 12 if age>=18 else 8

if age > 18:
    if((day == "Wednesday" or day== "wednesday")):
        price -= 2
        print("Your ticket price is $", price)
    else:
        print("Your ticket price is $", price)
    

