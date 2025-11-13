# Chapter 10: Python Basics - Practice Problems
# File Name: Chapter_10.py
print("Chapter 10: Python Basics - Practice Problems\n")

"""***** Questions On – Python Basics Practice Problems *****

    Questions:
        1-> Write a python script to print "Hello, World!" on the screen.
        2-> Write a python script to calculate the area of a rectangle. Length and breadth are given by user.
        3-> Write a python script to convert temperature from Celsius to Fahrenheit. Temperature value is given by user.
        4-> Write a python script to find maximum between two numbers. Numbers are given by user.
        5-> Write a python script to check whether a number is even or odd. Number is given by user.

    Answers:
        => All the answers are out of the Comment box.
"""

# Answer-1:
print("Solution of question-1")
print("Hello, World!")

# Answer-2:
print("\nSolution of question-2")
length = float(input("Enter length of the rectangle here : "))
breadth = float(input("Enter breadth of the rectangle here : "))
area = length * breadth
print("The area of rectangle is : ", area)

# Answer-3:
print("\nSolution of question-3")
celsius = float(input("Enter temperature in Celsius here : "))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in Fahrenheit is : ", fahrenheit)

# Answer-4:
print("\nSolution of question-4")
num1 = float(input("Enter first number here : "))
num2 = float(input("Enter second number here : "))
if num1 > num2:
    print("The maximum number is : ", num1)
elif num2 > num1:
    print("The maximum number is : ", num2)
else:
    print("Both numbers are equal.")

# Answer-5:
print("\nSolution of question-5")
number = int(input("Enter a number here : "))
if number % 2 == 0:
    print("The number %d is Even." % number)
else:
    print("The number %d is Odd." % number)
