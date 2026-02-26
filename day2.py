# Simple Calculator 

NUM1, NUM2 = float(input("Enter first number:" )), float(input("Enter second number: "))
operation = input("Select operation:(+, -, *, /): ")
#NUM2 = float(input("Enter a number: ")) #optimized

if operation == "+":
    result = NUM1 + NUM2
elif operation == "-":
    result = NUM1 - NUM2
elif operation == "*":
    result = NUM1 * NUM2
elif operation == "/":
    if NUM2 == 0:
        print("Error: Cannot divide by zero")
    else:
        result = NUM1 / NUM2
else:
    print("Invalid operator")

print(str(NUM1) + " " + operation + " " + str(NUM2) + " = " + str(result))
print(f"{NUM1} {operation} {NUM2} = {result}") #fstrings