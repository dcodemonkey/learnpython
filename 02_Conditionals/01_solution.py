age = input('Enter the age: ')

age_in_int = int(age)

if age_in_int < 13:
    print('You are a Child.')
elif age_in_int < 20:
    print('You are a teenager.')
elif age_in_int < 60:
    print('You are a Adult.')
else:
    print('You\'r a senior person.')
