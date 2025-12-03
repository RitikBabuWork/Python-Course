# Chapter : 14 - Advanced String Manipulations
# File name : Chapter_014.py
import string
print("Chapter 14: Advanced String Manipulations")
# Example of string splitting with different delimiter
str = "Ritik Verma"
words = str.split()
print(f"Split by whitespace: {words}")

# Split with custom delimiter
str2 = "apple,banana,orange"
fruits = str2.split(',')
print(f"Split by comma: {fruits}")

# Join strings
joined = " - ".join(fruits)
print(f"Joined with dash: {joined}")

# String case conversions
print(f"Uppercase: {str.upper()}")
print(f"Lowercase: {str.lower()}")
print(f"Title case: {str.title()}")

# String stripping
str3 = "  hello world  "
print(f"Original: '{str3}'")
print(f"Stripped: '{str3.strip()}'")

# String replacement
str4 = "Python is great, Python is fun"
replaced = str4.replace("Python", "Java")
print(f"Replaced: {replaced}")

# Find substring
position = str4.find("great")
print(f"Position of 'great': {position}")

# Check string content
print(f"Is alphabetic: {str.isalpha()}")
print(f"Is digit: {'12345'.isdigit()}")