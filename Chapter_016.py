# Chapter : 16 - List in Python
# File name : Chapter_016.py
print("Chapter 15: List in Python")
# Example of List operations in Python

# 1. Creating Lists
empty_list = []
list_with_values = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, None]
list_with_duplicates = [1, 2, 2, 3, 3, 3]

# 2. Accessing Elements
first_element = list_with_values[0]  # 1
last_element = list_with_values[-1]  # 5
slice_elements = list_with_values[1:4]  # [2, 3, 4]

# 3. Adding Elements
list_with_values.append(6)  # Add single element
list_with_values.extend([7, 8, 9])  # Add multiple elements
list_with_values.insert(0, 0)  # Insert at specific index

# 4. Removing Elements
list_with_values.remove(6)  # Remove by value
popped_element = list_with_values.pop()  # Remove and return last element
list_with_values.pop(0)  # Remove by index
list_with_values.clear()  # Remove all elements

# 5. List Methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()  # Sort in-place
reversed_list = numbers[::-1]  # Reverse using slice
count = numbers.count(1)  # Count occurrences
index = numbers.index(4)  # Find index of element
copy_list = numbers.copy()  # Create shallow copy

# 6. List Comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
nested = [[i*j for j in range(3)] for i in range(3)]

# 7. Iterating Through Lists
for element in numbers:
    print(element)

for index, element in enumerate(numbers):
    print(f"Index {index}: {element}")

# 8. List Unpacking
a, b, c = [1, 2, 3]
first, *middle, last = [1, 2, 3, 4, 5]

# 9. Sorting and Reversing
sorted_list = sorted(numbers)  # Returns new sorted list
numbers.sort(reverse=True)  # Sort descending
numbers.reverse()  # Reverse in-place

# 10. Checking Membership
is_present = 5 in numbers
is_not_present = 10 not in numbers

# 11. List Length and Sum
length = len(numbers)
total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)

# 12. Combining Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
combined_extend = list1 * 2  # Repeat list

# 13. Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
element = matrix[0][1]  # Access nested element

# 14. Lambda with Lists
numbers_lambda = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers_lambda))
filtered = list(filter(lambda x: x > 2, numbers_lambda))