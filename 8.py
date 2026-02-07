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