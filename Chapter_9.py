# Chapter 9: Operators in Python.
# File Name: Chapter_9.py
print("Chapter 9: Operators in Python.\n")

"""***** Questions On – Operators in Python *****

    Questions:
        1-> Write a python script to demonstrate use of arithmetic operators.
        2-> Write a python script to demonstrate use of comparison operators.
        3-> Write a python script to demonstrate use of assignment operators.
        4-> Write a python script to demonstrate use of logical operators.
        5-> Write a python script to demonstrate use of bitwise operators.

    Answers:
        => All the answers are out of the Comment box.
"""
# Answer-1:
print("Solution of question-1")
a = 15
b = 4
print("The value of a + b is : ", a + b)
print("The value of a - b is : ", a - b)
print("The value of a * b is : ", a * b)
print("The value of a / b is : ", a / b)
print("The value of a % b is : ", a % b)
print("The value of a ** b is : ", a ** b)
print("The value of a // b is : ", a // b)

# Answer-2:
print("\nSolution of question-2")
a = 10
b = 20
print("The value of a == b is : ", a == b)
print("The value of a != b is : ", a != b)
print("The value of a > b is : ", a > b)
print("The value of a < b is : ", a < b)
print("The value of a >= b is : ", a >= b)
print("The value of a <= b is : ", a <= b)

# Answer-3:
print("\nSolution of question-3")
a = 5
print("Initial value of a is : ", a)
a += 3
print("The value of a after a += 3 is : ", a)
a -= 2
print("The value of a after a -= 2 is : ", a)
a *= 4
print("The value of a after a *= 4 is : ", a)
a /= 3
print("The value of a after a /= 3 is : ", a)
a %= 5
print("The value of a after a %= 5 is : ", a)
a **= 2
print("The value of a after a **= 2 is : ", a)
a //= 4
print("The value of a after a //= 4 is : ", a)

# Answer-4:
print("\nSolution of question-4")
x = True
y = False
print("The value of x and y is : ", x and y)
print("The value of x or y is : ", x or y)
print("The value of not x is : ", not x)
print("The value of not y is : ", not y)

# Answer-5:
print("\nSolution of question-5")
p = 10  # In binary: 1010
q = 4   # In binary: 0100
print("The value of p & q is : ", p & q)   # Bitwise AND
print("The value of p | q is : ", p | q)   # Bitwise OR
print("The value of p ^ q is : ", p ^ q)   # Bitwise XOR
print("The value of ~p is : ", ~p)         # Bitwise NOT
print("The value of p << 2 is : ", p << 2) # Left Shift
print("The value of p >> 2 is : ", p >> 2) # Right Shift