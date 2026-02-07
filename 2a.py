# Name Formatter

A = input("Enter first name: ")
B = input("Enter second name: ")
age = int(input("Enter the age: "))

print(A, B, age)

# Temperature Converter

Celcius = float(input("Enter temperature in Celsius: "))
Fahrenheit = (Celcius * 9/5) + 32
print("Temperature in Fahrenheit:", Fahrenheit)

# Multi line Display

Line = input("Enter 3 words: ")
words = Line.split()
print(words[0])
print(words[1])
print(words[2])

# Shopping bill

item = input("Enter the name of item: ")
quantity = float(input("Enter the quantity: " ))
price = float(input("Enter the price: "))

total_amount = quantity * price
print(total_amount)