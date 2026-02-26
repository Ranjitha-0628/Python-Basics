#Logical Operations

a = 11
b = 20
print("Both numbers are greater than 10: " + str(a>10 and b>10))
print("At least one of the numbers is less than 5: " + str(a<5 or b>5))
print("The first number is not greater than the second: " + str(not(a > b )))

#Comparison Operations

age = int(input("Enter the age: "))
print("You are major: " + str(age >= 18))
print("Your are minor: " + str(age < 18))

# Membership operations

s = input("Enter the string: ")

# Check if the letter 'a' is in the string
print("Does the string contain 'a'?:", 'a' in s)# do not forget to give coats to the particular checking member

# Check if the string does not contain the word 'Python'
print("Does the string NOT contain 'z'?:", 'z' not in s)

#Bitwise Operaions

num1 = 50 
num2 = 100

print(int(num1 & num2))
print(num1 | num2)
print(num1 ^ num2)
print(num1 << 2)
print(num1 >> 1)
print(~num2)
