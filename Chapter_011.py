import re
from collections import Counter
import re
from itertools import zip_longest
import string
import re

# Chapter 11: Strings in Python.
# File Name: Chapter_11.py
print("Chapter 11: Strings in Python.\n")

"""***** Questions On – Strings in Python *****

    Questions:
        1-> Write a python script to print the length of a string.
        2-> Write a python script to print the last character of a string.
        3-> Write a python script to print the first character of a string.
        4-> Write a python script to print the last three characters of a string.
        5-> Write a python script to print the first five characters of a string.
        6-> Write a python script to print the characters between index 2 and 5 of a string.
        7-> Write a python script to print the string in reverse order.
        8-> Write a python script to print the string in uppercase.
        9-> Write a python script to print the string in lowercase.
        10-> Write a python script to print the string with the first letter of each word capitalized.
        11-> Write a python script to replace a substring in a string with another substring.
        12-> Write a python script to find the index of a substring in a string.
        13-> Write a python script to check if a substring exists in a string.
        14-> Write a python script to count the occurrences of a substring in a string.
        15-> Write a python script to split a string into a list of substrings based on a delimiter.
        16-> Write a python script to join a list of strings into a single string with a specified delimiter.
        17-> Write a python script to remove leading and trailing whitespace from a string.
        18-> Write a python script to check if a string starts with a specific substring.
        19-> Write a python script to check if a string ends with a specific substring.
        20-> Write a python script to count the number of words in a string.
        21-> Write a python script to reverse the order of words in a string.
        23-> Write a python script to check if a string is a palindrome.
        24-> Write a python script to find the largest word in a string.
        25-> Write a python script to find the smallest word in a string.
        26-> Write a python script to replace all occurrences of a substring in a string with another   substring.
        28-> Write a python script to convert a string to title case.
        29-> Write a python script to check if a string contains only alphabetic characters.
        30-> Write a python script to check if a string contains only numeric characters.
        31-> Write a python script to check if a string contains only alphanumeric characters.
        32-> Write a python script to find the frequency of each character in a string.
        33-> Write a python script to remove all vowels from a string.
        34-> Write a python script to count the number of sentences in a string.
        35-> Write a python script to capitalize the first letter of each sentence in a string.
        36-> Write a python script to find the second largest word in a string.
        37-> Write a python script to check if two strings are anagrams of each other.
        38-> Write a python script to find the common characters between two strings.
        39-> Write a python script to find the uncommon characters between two strings.
        40-> Write a python script to merge two strings by alternating their characters.
        41-> Write a python script to check if a string is a pangram.
        42-> Write a python script to find the longest palindromic substring in a string.
        43-> Write a python script to count the number of uppercase and lowercase letters in a string.
        44-> Write a python script to find the first non-repeating character in a string.
        45-> Write a python script to remove duplicate characters from a string.
        46-> Write a python script to check if a string is a valid email address.
        47-> Write a python script to check if a string is a valid URL.
        48-> Write a python script to find the longest word in a string without using built-in functions.
        49-> Write a python script to find the shortest word in a string without using built-in functions.
        50-> Write a python script to count the number of vowels and consonants in a string.

    Answers:
        => All the answers are out of the Comment box.
"""

# Answer-1:
text = "Hello World from Python Programming!"
print("1-> Length:", len(text))

# Answer-2:
print("2-> Last character:", text[-1])

# Answer-3:
print("3-> First character:", text[0])

# Answer-4:
print("4-> Last three characters:", text[-3:])

# Answer-5:
print("5-> First five characters:", text[:5])

# Answer-6:
print("6-> Characters between index 2 and 5:", text[2:6])

# Answer-7:
print("7-> Reverse:", text[::-1])

# Answer-8:
print("8-> Uppercase:", text.upper())

# Answer-9:
print("9-> Lowercase:", text.lower())

# Answer-10:
print("10-> Title case:", text.title())

# Answer-11:
print("11-> Replace substring:", text.replace("Python", "Java"))

# Answer-12:
print("12-> Index of 'Python':", text.find("Python"))

# Answer-13:
print("13-> 'Python' in text?:", "Python" in text)

# Answer-14:
print("14-> Occurrences of 'o':", text.count("o"))

# Answer-15:
words = text.split(" ")
print("15-> Split by space:", words)

# Answer-16:
joined = "-".join(words)
print("16-> Joined with '-':", joined)

# Answer-17:
s_with_spaces = "   trim me   "
print("17-> Stripped:", repr(s_with_spaces.strip()))

# Answer-18:
print("18-> Starts with 'Hello'?:", text.startswith("Hello"))

# Answer-19:
print("19-> Ends with '!'?:", text.endswith("!"))

# Answer-20:
print("20-> Number of words:", len(text.split()))

# Answer-21:
print("21-> Reverse order of words:", " ".join(text.split()[::-1]))

# Answer-23:
def is_palindrome(s):
    s2 = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return s2 == s2[::-1]
print("23-> Is palindrome ('Madam')?:", is_palindrome("Madam"))
print("23-> Is palindrome (text)?:", is_palindrome(text))

# Answer-24:
words_clean = [w.strip("!,.?;:") for w in text.split()]
largest = max(words_clean, key=len)
print("24-> Largest word:", largest)

# Answer-25:
smallest = min(words_clean, key=len)
print("25-> Smallest word:", smallest)

# Answer-26:
print("26-> Replace all 'o' with '0':", text.replace("o", "0"))

# Answer-28:
print("28-> Title case:", text.title())

# Answer-29:
alpha_test = "HelloWorld"
print("29-> Only alphabetic?:", alpha_test.isalpha())

# Answer-30:
num_test = "12345"
print("30-> Only numeric?:", num_test.isdigit())

# Answer-31:
alnum_test = "abc123"
print("31-> Only alphanumeric?:", alnum_test.isalnum())

# Answer-32:
freq = Counter(text)
print("32-> Frequency of each character:", dict(freq))

# Answer-33:
no_vowels = "".join(ch for ch in text if ch.lower() not in "aeiou")
print("33-> Without vowels:", no_vowels)

# Answer-34:
sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
print("34-> Number of sentences:", len(sentences))

# Answer-35:
def capitalize_sentences(s):
    parts = re.split(r'([.!?]\s*)', s)
    return "".join(p.capitalize() for p in parts)
multi = "hello. how are you? i'm fine!"
print("35-> Capitalize sentences:", capitalize_sentences(multi))

# Answer-36:
unique_words = list(dict.fromkeys(words_clean))
sorted_by_len = sorted(unique_words, key=len, reverse=True)
second_largest = sorted_by_len[1] if len(sorted_by_len) > 1 else ""
print("36-> Second largest word:", second_largest)

# Answer-37:
def are_anagrams(a, b):
    a2 = "".join(ch.lower() for ch in a if ch.isalnum())
    b2 = "".join(ch.lower() for ch in b if ch.isalnum())
    return sorted(a2) == sorted(b2)
print("37-> Anagrams ('listen','silent')?:", are_anagrams("listen", "silent"))

# Answer-38:
s1 = "apple"
s2 = "grape"
print("38-> Common characters:", set(s1) & set(s2))

# Answer-39:
print("39-> Uncommon characters:", set(s1) ^ set(s2))

# Answer-40:
a = "abc"
b = "12345"
merged = "".join(x or "" for pair in zip_longest(a, b) for x in pair)
print("40-> Alternating merge:", merged)

# Answer-41:
def is_pangram(s):
    letters = set(ch.lower() for ch in s if ch.isalpha())
    return set(string.ascii_lowercase) <= letters
print("41-> Is pangram ('The quick brown fox jumps over the lazy dog')?:", is_pangram("The quick brown fox jumps over the lazy dog"))

# Answer-42:
def longest_pal_substr(s):
    if not s:
        return ""
    start = 0
    end = 0
    for i in range(len(s)):
        # odd
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l > end - start:
                start, end = l, r
            l -= 1; r += 1
        # even
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l > end - start:
                start, end = l, r
            l -= 1; r += 1
    return s[start:end+1]
print("42-> Longest palindromic substring in 'babad':", longest_pal_substr("babad"))

# Answer-43:
upper_count = sum(1 for ch in text if ch.isupper())
lower_count = sum(1 for ch in text if ch.islower())
print("43-> Uppercase:", upper_count, "Lowercase:", lower_count)

# Answer-44:
def first_non_repeating(s):
    cnt = Counter(s)
    for ch in s:
        if cnt[ch] == 1:
            return ch
    return None
print("44-> First non-repeating char:", first_non_repeating("swiss"))

# Answer-45:
def remove_duplicates_preserve_order(s):
    seen = set()
    out = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            out.append(ch)
    return "".join(out)
print("45-> Remove duplicates:", remove_duplicates_preserve_order("banana"))

# Answer-46:
def is_valid_email(e):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, e) is not None
print("46-> Valid email ('user@example.com')?:", is_valid_email("user@example.com"))

# Answer-47:
def is_valid_url(u):
    pattern = r'^(https?://)?(www\.)?[\w\.-]+\.\w{2,}(/.*)?$'
    return re.match(pattern, u) is not None
print("47-> Valid URL ('https://example.com')?:", is_valid_url("https://example.com"))

# Answer-48:
def longest_word_no_builtins(s):
    longest = ""
    current = ""
    for ch in s + " ":
        if ch.isalpha():
            current += ch
        else:
            if len(current) > len(longest):
                longest = current
            current = ""
    return longest
print("48-> Longest word without split:", longest_word_no_builtins("Find the longestword here"))

# Answer-49:
def shortest_word_no_builtins(s):
    shortest = None
    current = ""
    for ch in s + " ":
        if ch.isalpha():
            current += ch
        else:
            if current:
                if shortest is None or len(current) < len(shortest):
                    shortest = current
            current = ""
    return shortest or ""
print("49-> Shortest word without split:", shortest_word_no_builtins("Find the tiny word here"))

# Answer-50:
def vowels_consonants(s):
    v = set("aeiouAEIOU")
    vowels = consonants = 0
    for ch in s:
        if ch.isalpha():
            if ch in v:
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants
v, c = vowels_consonants(text)
print("50-> Vowels:", v, "Consonants:", c)