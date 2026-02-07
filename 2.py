a = 10
b = 20

print(b)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

print(a+b-a*b/a%b+5)
print(a//b+a-b-a**b+7)

# swapping values of 2 variables using a third variable

_1number = int(input("Enter the first number: "))
_2number = int(input("Enter the second number: "))

print("Before swap: " + "First number = " + str(_1number) + " Second number = " + str(_2number))

temp =_1number
_1number = _2number
_2number = temp

print("After swap: " + "First number = " + str(_1number) + " Second number = " + str(_2number))

# swapping values of 2 variables without using a third variable

num1 = int(input("Give 1st number: "))
num2 = int(input("Give 2nd number: "))

print("Before swapping: " + "1st = " +str(num1) + " 2nd = " +str(num2))

num1 , num2 = num2, num1

print("After swapping: " + "1st = ," +str(num1) + " 2nd = ," +str(num2))