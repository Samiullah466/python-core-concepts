# 💻 Bootcamp Week 1 - Day 1 Lab
### Python Fundamentals & Data Structures
Welcome to the Day 1 lab session! This lab will reinforce your understanding of core Python syntax and data structures. Complete each section step by step.

## 🔸 Step 1: Variables & Data Types
Create variables of different types and observe their behavior.
"""

# TODO: Define a string, integer, float, and boolean
# Hint: Use type() to verify the type of each variable
name = 'Sami Ullah'
age = 25
height = 5.3
is_student = False

# Print each variable and its type

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

"""## 🔸 Step 2: Conditional Statements
Write a simple program to evaluate a student's grade.
"""

# TODO: Ask user to enter a score (0-100) and print the grade
# Hint: Use if-elif-else ladder
score = int(input("Enter your score: "))
# Add grading logic here
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

"""## 🔸 Step 3: Loops & Pattern Printing
Use loops to generate simple patterns.
"""

# TODO: Print a right-angled triangle using '*'
n = 5  # height of triangle
for i in range(1, n+1):
    print('*' * i)

"""## 🔸 Step 4: Lists & Comprehensions
Create and manipulate lists using Pythonic techniques.
"""

# TODO: Create a list of squares from 1 to 10 using list comprehension
squares = [ ]  # Fill this
for i in range(1, 11):
    squares.append(i**2)
print(squares)

"""## 🔸 Step 5: Tuples, Sets, and Dictionaries
Explore basic operations on key Python data structures.
"""

# TODO: Create a tuple of 5 items, add values to a set, and use a dictionary
sample_tuple = ('red', 'green', 'blue', 'yellow', 'purple')  # Fill tuple
sample_set = set()
sample_set.add('apple')
sample_set.add('banana')
sample_dict = {'name': 'Alice', 'age': 25}

print("Tuple:", sample_tuple)
print("Set:", sample_set)
print("Dictionary:", sample_dict)

"""## 🔸 Step 6: Challenge - Word Frequency Counter
Write a Python program that counts the frequency of each word in a string.
"""

# TODO: Word frequency counter using dictionary
text = "Python is simple yet powerful. Python is easy to learn."

# Remove punctuation and convert to lowercase
text = text.replace('.', '').lower()

# Split text and count frequency
words = text.split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
# Fill the logic here to count words
print(word_freq)

"""## 🔸 Step 7 (Optional): List Mutability in Functions
Pass a list to a function and modify it. Observe the changes.
"""

# TODO: Define a function that appends items to a list and observe mutability
def modify_list(my_list):
    my_list.append("new item")

lst = ["item1", "item2"]
modify_list(lst)
print(lst)

