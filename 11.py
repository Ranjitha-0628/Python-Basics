#Lambda Functions

multiply = lambda a, b : (a * b)
print(multiply(2,3))

modulus = lambda x,y : x % y
result = modulus(5, 10)
print(result)

square = lambda p : p ** 2
print(square(4))

double = lambda q : 2 * q
print(double(5))

#Recursive Function to calculate first n numbers
def sum_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n-1)
print(sum_of_numbers(10))

n = 10 #Python shortcut same question 
print(sum(range(1, n+1)))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci (n-1) + fibonacci (n-2)
    
N = int(input("Enter the number: "))
fibonacci_sequence = [fibonacci(i) for i in range(N)]
print(fibonacci_sequence)

#Variable length arguments
def average(*numbers):
    if not numbers: # to avoid zero division error
       return 0

    total = sum(numbers)
    count = len(numbers)
    return total/count

print(average(10,20,30,40,50))