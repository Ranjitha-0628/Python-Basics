#Simple greeting program
name = input("Enter the name: ")
age = input("Enter the age: ")

#using concatenation symbol(+)
print("Output: " + "Hello, this is " + name + " and im " + age + " years old")

#using formatted strings
print(f"Hello this is {name} and i am {age} years old.")

#String manipulation
sentence = input("ENTER THE SENTENCE: ")

print(sentence.lower())
print(sentence.upper())
print(sentence.replace(" ", "_"))
print(sentence.strip())


# Escape sequences 
sen = input("Enter a string: ") #approch1
print("Hello\n\tWorld\nThis is a backslash: \\")

sen = input("Enter a string: ") #approch2
print("Hello")
print("\tWorld")
print("This is a backslash: \\")

# Count characters excluding spaces // replace operation to remove spaces
s = input("Enter a string to count characters (spaces ignored): ")
count = len(s.replace(" ", ""))
print(f"Number of characters (excluding spaces): {count}")