distance = 100

if distance < 3:
    mode_transport = "Walk"   
elif distance <= 15:
    mode_transport = "Bike"
else:
    mode_transport = "Car"

print("AI recommends you are the transport of",mode_transport + ".")