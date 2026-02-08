# Program to print even numbers 1 to 10
i = 1
for i in range(1,11):
    if i%2==0:
     print(i, end=" ")
# Check positive, negative, zero 
i = int(input("Enter a number: "))

if i < 0:
    print("Number is negative")
elif i > 0:
    print("Number is positive")
else:
    print("Zero")
    
#Print "Hello" 5 times using a loop     
#using while loop 
i = 1
while i <= 5:
    print("Hello")
    i += 1

#using for loop 

for i in range(5):
    print("Hello")

#Bus fare
age = int(input("Enter the age: "))
if age < 5:
    print("Bus pass is free!")
elif age >= 60:
    print("Get senior discount!")
else:
    print("Pay full fare!")

#Meal tracker
time = int(input("Enter the time: "))

if time == 8:
    print("Its breakfast time")
elif time == 1:
    print("Its lunch time")
elif time == 20:
    print("Its dinner time")
else:
    print("Its not meal time")

#Voting eligibility

membership = int(input("Enter the age: "))
if membership < 18:
    print("Student membership!")
elif membership >= 60:
    print("Senior membership!")
else:
    print("Regular membership!")