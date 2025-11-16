# Chapter 4: Type Conversion in Python.
# File Name: Chapter_5.py
print("Chapter 5: Type Conversion in Python.\n")

# Type Conversion:
# Converting a value from one data type to another (e.g., int, float, str, bool).
# Implicit conversion: Python automatically converts compatible types (e.g., int -> float).
# Explicit conversion (casting): use conversion functions like int(), float(), str(), bool(), chr(), ord().
# Notes:
# - Converting float -> int truncates the fractional part (possible precision loss).
# - Some conversions are invalid and raise errors (e.g., int("abc") -> ValueError).
# - bool conversion: 0 and empty containers/strings -> False, all other values -> True.
# - ord(char) gives Unicode code point; chr(code) gives character for a Unicode code point.

"""
***** Questions On – type conversion *****

    Questions:
        1-> Write a python script to convert a number into str type.
        2-> Write a python script to print Unicode of character ‘m’.
        3-> Write a python script to print character representation of a given Unicode 100.
        4-> Write a python script to convert a str type data into an int type. Also describe
            when a str type value in not possible to convert into an int type.
        5-> How to convert an integer value into a bool value.

    Answers:
        => All the answers are out of the Comment box.
"""

# Answer-1:
print("Solution of question-1")
a = 12
print("This is the conversion of int type a= %d into Str type : %s\n"%(a, str(a)))


# Answer-2:
print("\nSolution of question-2")
print("The unicode of 'm' is : ", ord('m'))


# Answer-3:
print("\nSolution of question-3")
print("The character of 100 unicode is : ", chr(100))


# Answer-4:
print("\nSolution of question-4")
a = "143"
print("The conversion of str value to int type is : ", int(a))
a = "Ritik" # This string will never convert into int type because of it's a real string value so it can't change.


# Answer-5:
print("\nSolution of question-5")
print("This is the conversion of int type value into bool type value : ", bool(234))
print("This is the conversion of int type value into bool type value : ", bool(0))
print("This is the conversion of int type value into bool type value : ", bool(12345))
