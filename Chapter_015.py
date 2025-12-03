# Chapter : 15 - Conditional Statements in Python
# File name : Chapter_015.py
print("Chapter 15: Conditional Statements in Python")
# Example of basic if-else statement
num = 10

# Basic if-else
if num > 0:
    print("Number is positive")
else:
    print("Number is not positive")

# if-elif-else
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Nested if-else
if num > 0:
    if num > 5:
        print("Number is positive and greater than 5")
    else:
        print("Number is positive but less than or equal to 5")

# Ternary operator
result = "Even" if num % 2 == 0 else "Odd"
print(f"{num} is {result}")

# Using and/or operators
if num > 5 and num < 15:
    print("Number is between 5 and 15")

if num == 10 or num == 20:
    print("Number is either 10 or 20")

# Using not operator
if not num < 0:
    print("Number is not negative")

# Membership test
numbers = [5, 10, 15, 20]
if num in numbers:
    print(f"{num} is in the list")