#For loops
#Printing multiples of 3 from 1 to 30
for i in range(1,30):
    if i%3 ==0:
        print("Multiples of 3: " + str(i), end =" ")
        print(f"3 * {i} = {i*3}")

# Sum of first 10 numbers
total = 0
for i in range(1, 11):
    total += i

print("Sum of first 10 numbers:", total)

#Printing each letter in a name
name = (input("Enter your name: "))
for letter in name:
    print(letter)

#Count vowels in a string
name = (input("Enter your name: "))
vowels = "aeiouAEIOU"
count = 0
for letter in name:
    if letter in vowels:
        count += 1
print("Number of vowels in the name: ", count)