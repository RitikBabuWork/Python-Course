import string

# Chapter 12: String Slicing and Manipulation
# File name : Chapter_012.py
print("Chapter 12: String Slicing and Manipulation")
# Example of string splitting
str = "Ritik Verma"
word = str.split(" ")
print(word)
print(str)
# Example of string slicing
# Example of string slicing and manipulation - additional examples

s = "  Hello, Ritik Verma! Welcome to Chapter 12.  \n"
print("Original:", repr(s))

# Basic indexing and slicing
print("s[0]:", s[0])
print("s[0:5]:", s[0:5])
print("s[:5]:", s[:5])
print("s[7:17]:", s[7:17])
print("s[-8:]:", s[-8:])
print("s[:-1]:", s[:-1])

# Slicing with step
print("s[::2]:", s[::2])
print("s[1::2]:", s[1::2])
print("Reversed s[::-1]:", s[::-1])

# Immutability: show how to "change" a character by creating a new string
lst = list(s)
lst[2] = 'X'
new_s = "".join(lst)
print("Modified via list:", new_s)

# Trimming whitespace
print("strip():", repr(s.strip()))
print("lstrip():", repr(s.lstrip()))
print("rstrip():", repr(s.rstrip()))

# Case conversions
print("lower():", s.lower())
print("upper():", s.upper())
print("title():", s.title())
print("capitalize():", s.strip().capitalize())
print("swapcase():", "PyTHon".swapcase())

# Replacement and translation
print("replace('Ritik', 'R.'):",
    s.replace("Ritik", "R."))
trans_table = str.maketrans("aeiou", "12345")
print("translate vowels->digits:", s.lower().translate(trans_table))

# Splitting and joining
words = s.split()  # default splits on whitespace
print("split():", words)
csv = "one,two,three"
print("split(','):", csv.split(","))
print("join with '-':", "-".join(words))

# partition and rpartition
head, sep, tail = s.partition("Welcome")
print("partition:", (head, sep, tail))
print("rpartition on ' ':", s.rpartition(" "))

# Searching
print("find('Ritik'):", s.find("Ritik"))
try:
    print("index('Ritik'):", s.index("Ritik"))
except ValueError:
    print("index: not found")
print("rfind(' '):", s.rfind(" "))
print("count('a'):", s.count("a"))

# Starts/ends and membership
print("starts with '  He':", s.startswith("  He"))
print("ends with '12.\\n':", s.endswith("12.\n"))
print("'Chapter' in s:", "Chapter" in s)

# Character tests
token = "Python3"
print("isalnum():", token.isalnum())
print("isalpha() on 'abc':", "abc".isalpha())
print("isnumeric() on '123':", "123".isnumeric())
print("isspace() on '   \\n':", "   \n".isspace())

# Formatting examples
name = "Ritik"
chap = 12
print("format():", "Name: {}, Chapter: {}".format(name, chap))
print("f-string:", f"Name: {name}, Chapter: {chap:02d}")

# Alignment and padding
print("center(40,'*'):", s.strip().center(40, "*"))
print("ljust(30):", "left".ljust(30, "-"))
print("rjust(30):", "right".rjust(30, "."))
print("zfill(5):", "42".zfill(5))

# Escape sequence vs raw string
print("escaped newline:", "Line1\nLine2")
print("raw string:", r"Line1\nLine2")

# Bytes and encoding
b = s.encode("utf-8")
print("encoded bytes:", b)
print("decoded back:", b.decode("utf-8"))

# splitlines
multiline = "first line\nsecond line\r\nthird line"
print("splitlines():", multiline.splitlines())

# Remove punctuation (simple)
no_punct = s.translate(str.maketrans("", "", string.punctuation))
print("without punctuation:", no_punct)

# Palindrome check (ignoring non-letters and case)
sample = "A man, a plan, a canal: Panama"
filtered = "".join(ch.lower() for ch in sample if ch.isalpha())
print("is palindrome:", filtered == filtered[::-1])

# Iterate characters with index
for i, ch in enumerate("ABC"):
    print(f"char {i} -> {ch}")

# Demonstrate maxsplit and rsplit
nums = "1 2 3 4 5"
print("split maxsplit=2:", nums.split(" ", 2))
print("rsplit maxsplit=2:", nums.rsplit(" ", 2))