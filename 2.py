a = 10
b = 20

print(b)

print(a+b)
print(a-b)
print(a*b) #asterisk or multiplicaion operator
print(a/b) 
print(a//b) #floor division operator
print(a%b) 
print(a**b) #Exponentiation operator

print(a+b-a*b/a%b+5)
print(a//b+a-b-a**b+7)

# swapping values of 2 variables using a third variable

_1number = int(input("Enter the first number: "))
_2number = int(input("Enter the second number: "))

print("Before swap: " + "First number = " + str(_1number) + " Second number = " + str(_2number))
print(f"Before Swap: \nFirst number = {_1number} Second number = {_2number}") # fStrings
temp =_1number # Store _1number in temp
_1number = _2number # Assign value of _2number to _1number
_2number = temp # Assign value of temp to _2number

print("After swap: " + "First number = " + str(_1number) + " Second number = " + str(_2number))

# swapping values of 2 variables without using a third variable

num1 = int(input("Give 1st number: "))
num2 = int(input("Give 2nd number: "))

print("Before swapping: " + "1st = " +str(num1) + " 2nd = " +str(num2))

num1 , num2 = num2, num1

print("After swapping: " + "1st = ," +str(num1) + " 2nd = ," +str(num2))