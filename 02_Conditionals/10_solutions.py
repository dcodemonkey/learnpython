pet = str(input("Enter the Pet type and age:"))
age = int(input("Enter the age of your pet:"))
petfood = ['Puppy Food', 'Senior Cat Food']

if(pet == "Dog" and age < 2):
    print("Your pet's recommended food is:", petfood[0])
elif(pet == "Cat" and age > 5):
    print("You Pet's recommended food is:", petfood[1])
else:
    print("We're really! As of now we don't have any food recommendation available for your pet.")