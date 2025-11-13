# Chapter 4: Variable and Keywords
# File name : Chapter_4.py
print("Chapter 4: Variable and Keywords\n")
print("Exercise Questions and Answers\n")

"""
***** Questions On – import and keywords *****

    Questions:
        1-> Write a python script to print all the keywords on the screen.
        2-> Use help section on python shell to see all the keywords.
        3-> Create two Python files A0.py and A1.py, Create a variable in A1.py and assign some value to it.
            Write a python script to import A1 module in A0 and print value of the variable created in A0.py.
        4-> Out of all the keywords, name those keywords which are used as data.
        5-> What is the use of del keyword?

    Answers:
        => All the answers are out of the Comment box.
"""

# Answer-1:
print("Solution of question-1")

import keyword

# from keyword import kwlist  # => We can also done this task.

print("This is the list of Python Keywords.\n", keyword.kwlist, "\n")

# Answer-2:
print("Solution of question-2\n")
"""
=> Print keywords list using Terminal.
    -> step-1. Open Machine your terminal. 
    -> step-2. type python and hit enter to just in pyton mode your terminal.
    -> step-3. type help() and hit enter.s
    -> step-4. type keywords and hit enter.
    -> Then this will so you all the list of Python keywords on the terminal screen.
"""

# Answer-3:
print("Solution of question-3\n")
"""
=> A0.py and A1.py file is the solution of this question.
    -> Your can check it out in the A0.py and A1.py file.
    -> I have solved this question using A0.py and A1.py file.
"""

# Answer-4:
print("Solution of question-4")
"""
There are only three keywords which can be used as data.
    1-> True
    3-> False
    3-> None
"""
t = True
f = False
n = None
print("T contains : ", t)
print("F contains : ", f)
print("N contains : ", n, "\n")

# Answer-5:
print("Solution of question-5")
"""
=> The use of (del) keyword in Python.
    -> (del)- keyword is used to delete created variable in Python.
    -> and if we don't want to delete any variable of python this don't worry python will automatically delete variable.
    
    like as: out of the comment lines.
"""
x = 20
print("The value of X is : ", x)
del x
# print("The value of X is : ", x) # => Now we can access variable X because of del x. if we will use it
# this will throw an error.




# Other Questions From Chapter-4.py:

# Question 1: What are keywords in Python? Using the keyword library, print all the Python keywords.
import keyword
print("Question 1: What are keywords in Python? Using the keyword library, print all the Python keywords.")
print("Answer:")
print(keyword.kwlist)
print("\n")
# Question 2: What are the rules to define a variable in Python?
print("Question 2: What are the rules to define a variable in Python?")
print("Answer:")
print("1. A variable name must start with a letter (a-z, A-Z) or an underscore (_).")
print("2. The rest of the variable name can contain letters, digits (0-9), or underscores.")
print("3. Variable names are case-sensitive (e.g., myVar and myvar are different).")
print("4. Variable names cannot be the same as Python keywords.")
print("\n")
# Question 3: What are the standards and conventions followed for defining variable in Python to improve code readability and maintainability?
print("Question 3: What are the standards and conventions followed for defining variable in Python to improve code readability and maintainability?")
print("Answer:")
print("1. Use meaningful and descriptive names that convey the purpose of the variable.")
print("2. Follow the snake_case convention for variable names (e.g., my_variable_name).")
print("3. Avoid using single-character variable names except for counters or iterators.")
print("4. Use lowercase letters for variable names.")
print("5. Avoid using special characters or spaces in variable names.")
print("\n")
# Question 4: What will happen if a keyword is used as a variable name?
print("Question 4: What will happen if a keyword is used as a variable name?")
print("Answer:")
print("If a keyword is used as a variable name, it will result in a syntax error because keywords are reserved words in Python and cannot be used for variable names.")
print("\n")