#Geet function // without arguments
def Greeting():
    print("Hello, This is Ranjitha!")
Greeting()

#Parameterized greet
def greet_user(name):
    print(f"Hi {name} Good morning!")
greet_user("Ranju")

#Sum Function 
def add_numbers(a, b):
    return a + b
result = add_numbers(10, 20)
print("Sum of numbers:" ,result)

#Area of circle
import math
def area_of_circle(radius):
    if radius < 0:
        print("radius cannot be negative")
    area = math.pi * (radius**2)
    return area
radius = 5
print("Area of circle: ", area_of_circle(radius))
