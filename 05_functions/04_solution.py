import math

def circle_stats(radius):
    # print('hi')
    area = math.pi * radius ** 2
    area = round(area, 2)
    circumference = 2 * math.pi * radius
    circumference = round(circumference, 2)
    return area, circumference
    
a, c = circle_stats(3)
print("Area: ", a, "Circuference: ", c)