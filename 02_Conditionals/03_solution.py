marks = int(input('Enter the marks to know your grade:'))
grade = ['A', 'B', 'C', 'D', 'F']

if(marks >= 101):
    print("Please verify your marks and Try again!")
    exit
elif(marks >= 90 and marks <= 100):
    print("Your grade is:", grade[0])
elif(marks >= 80 and marks <= 89):
    print("Your grade is:", grade[1])
elif(marks >= 70 and marks <= 79):
    print("Your grade is:", grade[2])
elif(marks >= 60 and marks <= 69):
    print("Your grade is:", grade[3])
else:
    print("Oops! You need to work hard. Your Grade is", grade[4])