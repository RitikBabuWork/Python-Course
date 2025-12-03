# Chapter : 13 - String Methods and Functions
# File name : Chapter_013.py
import string
print("Chapter 13: String Methods and Functions")
# Example of string splitting
str = "Ritik Verma"
print("Original string:", str)
print("Split string:", str.split())
print("Uppercase:", str.upper())
print("Lowercase:", str.lower())
print("Capitalized:", str.capitalize())
print("Title case:", str.title())
print("Length:", len(str))
print("Replace:", str.replace("Ritik", "John"))
print("Find position:", str.find("Verma"))
print("Reversed:", str[::-1])