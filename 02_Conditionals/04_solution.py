fruit = str(input("Enter the Fruit name:"))
color = str(input("What type of color you fruit has now:"))

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Ovveripe")
else:
    print("We don't have capacity to predict this fruit.")