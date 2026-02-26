#List Manipulation 
#List Kannada foods
kannada_foods = ["Ragi mudde", "Masala dose", "Bisi bele bath", "Mysore pak"]
print("Kannada foods: ", kannada_foods)

uppercase_foods = [item.upper() for item in kannada_foods]
print("Uppercase Kannada foods: ", uppercase_foods)

#Sum of prices
dict = {
      "sugar": 30,
      "salt": 20,
      "rice": 50,
      "wheat": 40
      }
#using for loop
total_price = 0
for price in dict.values():
    total_price += price
print(total_price)
#other method
total_price = sum(dict.values())
print(total_price) # using sum() function

#List of numbers 1 to 10, use list compreshension to create their squares
numbers = list(range(1, 11))
squares = [num ** 2 for num in numbers]
print("Squares of numbers from 1 to 10: ", squares)

#Student data task
s1 = {
    "name": "ranjitha",
    "age": 21,
    "marks": 94
    }
s2 = {
    "name": "keerthana",
    "age": 20,
    "marks": 89
}
s3 = {
    "name": "vaishnavi",
    "age": 22,
    "marks": 97
}
# Loop through the list and print each student's information.
students = [s1, s2, s3]
for student in students:
    print("Name: ", student["name"])
    print("Age: ", student["age"])
    print("Marks: ", student["marks"])

#Dictionary comprehension 
cities_in_karnataka = {
    "Bangalore": 1000000,
    "Mysore": 8000000,
    "Mangalore": 6000,
    "Madikeri":40000
    }

# using dictionary comprehension to filter out cities with populations below 10 lakhs.
filtered_cities = {
    city: population for city, population in cities_in_karnataka.items() if population >= 1000000
}
print(filtered_cities)

#Nested List Challenge

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Matrix row by row")
for row in matrix:
    print(*row)

print("Sum of each row")
for i, row in enumerate(matrix,start = 1):
    row_sum = sum(row)
    print("Sum of Row", i ,":", row_sum)