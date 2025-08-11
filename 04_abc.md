# Python Programming Quick Study Guide

## Table of Contents
- [Text & File Handling](#text--file-handling)
- [IDE & Code Editors](#ide--code-editors)
- [Python Operators](#python-operators)
- [Python Input/Output (I/O)](#python-inputoutput-io)
- [Data Types](#data-types)
- [Syntax & Indentation Rules](#syntax--indentation-rules)
- [Variables & Data Types](#variables--data-types)

---

## Text & File Handling

### Setting Up Python & IDEs

**Python Installation:**
- Python can be installed on Windows, Mac, or Linux
- Use version control with Git
- Install text editors or IDEs for development
- Consider using virtual environments

**File Operations:**
- Use built-in file handling functions
- Read and write text files
- Handle CSV and other data formats
- Manage file paths and directories

### Basic Syntax Rules

**Basic Programming Rules:**
- Use proper indentation (4 spaces recommended)
- Follow PEP 8 style guidelines
- Use meaningful variable names
- Comment your code appropriately

**Quick Tips:**
- Start with simple programs
- Practice with small projects
- Use online resources and documentation
- Join Python communities for support

---

## IDE & Code Editors

### Popular Python IDEs
- **PyCharm**: Full-featured IDE with debugging
- **VS Code**: Lightweight with Python extensions
- **IDLE**: Built-in Python environment
- **Jupyter Notebook**: Great for data analysis
- **Sublime Text**: Fast text editor with plugins

### Code Editor Features
- Syntax highlighting
- Code completion
- Debugging tools
- Version control integration
- Plugin ecosystem

---

## Python Operators

### 1. Arithmetic Operators
Used to perform basic math operations on values:
- `+` adds two values
- `-` subtracts one value from another
- `*` multiplies two values
- `/` divides and returns a float
- `//` performs floor division (removes decimal)
- `%` returns the remainder
- `**` performs exponentiation (power)

**Example:**
```python
a = 10, b = 3
b = 10 // 3  # 3
```

### 2. Comparison Operators
Compare values and return True or False:
- `==` checks if values are equal
- `!=` checks if they are not equal
- `<` checks if left is less than right
- `>` checks if left is greater
- `<=` checks if left is less than or equal
- `>=` checks if left is greater than or equal

**Example:**
```python
5 > 3  # True
```

### 3. Assignment Operators
Used to assign values to variables, often with arithmetic:
- `=` assigns a value
- `+=` adds and assigns
- `-=` subtracts and assigns
- `*=` multiplies and assigns
- `/=` divides and assigns
- `%=` finds remainder and assigns
- `**=` raises power and assigns

**Example:**
```python
x = 10, x += 2  # x is 12
```

### 4. Logical Operators
Used for combining conditional statements:
- `and` returns True if both are true
- `or` returns True if at least one is true
- `not` inverts the result

**Example:**
```python
a = True and False  # False
is not True  # False
```

### 5. Identity Operators
Used to check if two variables refer to the same object in memory:
- `is` returns True if they are the same
- `is not` returns True if not the same

**Example:**
```python
x = ["apple"]
y = ["apple"]
x is y  # False
```

### 6. Membership Operators
Used to check if a value exists in a sequence:
- `in` returns True if present
- `not in` returns True if not present

**Example:**
```python
"H" in "apple"  # True
5 not in [1, 2, 3]  # True
```

### 7. Bitwise Operators
Operate on bits:
- `&` AND
- `|` OR
- `^` XOR
- `~` NOT
- `<<` left shift
- `>>` right shift

### 8. Python Comments

**Single-Line Comments:**
A single-line comment starts with the `#` symbol. Everything after `#` on that line is ignored.

**Usage:**
- Explain what a line of code does
- Leave notes for yourself or other developers

**Example:**
```python
# This is a single-line comment
x = 5  # Assigning value to x
```

**Multi-line Comments:**
Python doesn't have official multi-line comment syntax like some other languages, but you can use one of two common approaches:

1. **Using multiple lines:**
Most common and clear for short explanations

2. **Using triple quotes:**
```python
"""
This block is ignored
by the interpreter and works
like a multi-line comment
"""
```

**Note:** Triple-quote comments are sometimes used for documentation strings (docstrings), but using `#` is more consistent for actual commenting.

---

## Python Input/Output (I/O)

### Python Input/Output
Python provides simple ways to handle user input and display output, making interaction with programs straightforward.

### Output: print() Function
Used to display text or variable values to the screen.

**Syntax:** `print("Hello, World!")`

You can also print variables:
```python
name = "Aamir"
print("Name:", name)
```

Use `,` to print multiple values:
```python
print("Age:", 25, "Years")
```

**Custom separator and end:**
```python
print("A", "B", "C", sep="-")  # Output: A-B-C
print("Hello", end=" ")  # Output without newline
print("World!")  # Output: Hello World!
```

### Input: input() Function
Used to take user input from the keyboard. Input is always read as a string.

**Syntax:**
```python
user_input = input("Enter something: ")
```

**Convert input to number if needed:**
```python
age = int(input("Enter your age: "))  # Convert input to integer
price = float(input("Enter price: "))  # Convert input to float
```

### Quick Tip:
Combine input and processing:
```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

Keep in mind: input() lets programs flow until the user types something and hits Enter.

### Typecasting in Python

Typecasting (also called type conversion) is the process of converting the data type of a variable from one type to another, as far as from string to integer, or integer to float. Python provides built-in functions to handle this safely.

**Why Typecasting?**
Python is a dynamically typed language, so you can change types as needed at runtime. But sometimes you need specific types, especially when taking user input (which is always a string).

**Common Typecasting Functions:**
- `int()` → Converts to Integer
- `float()` → Converts to float
- `str()` → Converts to string
- `bool()` → Converts to boolean

**Examples:**

**String to Integer:**
```python
age = int("25")  # Now age is an integer
```

**Float to Integer:**
```python
x = int(7)  # (decimal is removed, not rounded)
# x = 7
```

**Integer to String:**
```python
num = 10
text = str(num)  # "10"
```

**String to Float:**
```python
price = float("99.99")  # price is 99.99
```

**To Boolean:**
```python
bool(0)  # False
bool("hi")  # True
```

**Invalid Conversions:**
Not all conversions are valid. Trying to convert a non-numeric string to int or float causes an error.

Always validate or use try-except blocks for user input.

---

## Data Types

### 1. List (Ordered, Mutable)
A list holds a collection of items (any type) and maintains their order.

**Syntax:**
```python
fruits = ["apple", "banana", "cherry"]
```

**Access:** `fruits[0]  # "apple"`
**Modify:** `fruits[1] = "mango"`
**Add:** `fruits.append("grape")`
**Remove:** `fruits.remove("banana")`
**Length:** `len(fruits)`

### 2. Tuple (Ordered, Immutable)
Like a list, but cannot be changed after creation. Useful for fixed collections.

**Syntax:**
```python
coordinates = (10, 20)
```

**Access with index:** `coordinates[1]  # 20`
**Cannot be changed:** `coordinates[0] = 30  # Error!`
**Can be unpacked:** `x, y = coordinates`

### 3. Set (Unordered, Unique)
A set stores unique items, removing duplicates automatically.

**Syntax:**
```python
nums = {1, 2, 3}
# Result: {1, 2}
# Add: nums.add(4)
# Remove: nums.remove(2)
```

### 4. Dictionary (Key-Value Pairs)
Stores data in key-value format. Very useful for lookups.

**Syntax:**
```python
student = {"name": "Aamir", "age": 21}
```

**Access:** `student["name"]  # "Aamir"`
**Modify:** `student["age"] = 22`
**Add:** `student["grade"] = "A"`
**Remove:** `del student["age"]`

---

## Syntax & Indentation Rules

### Correct:
```python
age = 18
if age >= 18:
    print("You can vote!")
    print("You are an adult")
else:
    print("Too young to vote")
```

### Error Prone Content:
An error may occur if there are no consistent indentations. This is one statement.

### Block Friendly Python Methods Used:
For Python functions, numbers are inside work. 
For Python statements inside work a...

**Quick Tips:**
- Use consistent indentation (4 spaces recommended)
- Python relies on indentation to define code blocks
- Mix of tabs and spaces can cause errors
- Use a good text editor that shows whitespace

### Why Type-check Python:
Python tries to be as Python as possible but will throw syntax which can prevent operations and easily to use.

---

## Variables & Data Types

### Variables & Data Types

In Python, you don't need to explicitly declare variable types - Python figures this out automatically.

**Creating Variables:**
```python
name = "Python"
age = 30
height = 5.9
is_student = True
```

**Variable Naming Rules:**
- Must start with a letter or underscore
- Can contain letters, numbers, and underscores  
- Case sensitive (`Name` and `name` are different)
- Cannot use Python keywords

**Data Types:**
- **String (str):** Text data `"Hello"`
- **Integer (int):** Whole numbers `42`
- **Float (float):** Decimal numbers `3.14`
- **Boolean (bool):** True/False values
- **List:** Ordered collection `[1, 2, 3]`
- **Dictionary:** Key-value pairs `{"key": "value"}`

**Check Type:**
```python
type(variable_name)  # Returns the data type
```

**Multiple Assignment:**
```python
x, y, z = 1, 2, 3
```

---

## Slicing, Formatting & Common Methods in Python

### Slicing (Strings & Lists)
Slicing allows you to extract a portion of a list or string using the format: `object[start:stop:step]`

- `start`: index to begin (inclusive)
- `stop`: index to end (exclusive)
- `step`: how many steps to jump

**Examples:**
```python
text = "Python"
text[1:4]    # "yth"
text[:4]     # "Pyth" (from start)
text[2:]     # "thon" (till end)
text[::-1]   # "nohtyP" (reversed)

nums = [10, 20, 30, 40, 50]
nums[1:4]    # [20, 30, 40]
```

### String Formatting
Python has multiple ways to format strings dynamically:

**f-Strings (Recommended, Python 3.6+):**
```python
name = "Aamir"
age = 25
print(f"My name is {name} and I'm {age}")
```

**Format Method:**
```python
print("My name is {} and I'm {}".format(name, age))
```

**Old Style (% formatting):**
```python
print("My name is %s and I'm %d" % (name, age))
```
*f-strings are fastest and most readable.*

### Common String Methods
Strings in Python are immutable, but many methods return a new string:

- `lower()` → converts to lowercase
- `upper()` → converts to uppercase
- `strip()` → removes spaces from ends
- `replace(old, new)` → replaces substrings
- `split()` → splits string into a list
- `join()` → joins list into string
- `find(sub)` → returns index of substring
- `startswith() / endswith()` → checks prefixes/suffixes

**Example:**
```python
text = " Hello Python "
clean = text.strip().lower()  # "hello python"
```

### Common List Methods
Lists are mutable – you can modify them in place:

- `append(item)` → adds to end
- `insert(i, item)` → adds at index
- `remove(item)` → removes first match
- `pop(i)` → removes at index
- `sort()` → sorts list in-place
- `reverse()` → reverses list
- `count(item)` → how many times item appears
- `index(item)` → finds index of item

**Example:**
```python
names = ["Ali", "Zara", "Ali"]
names.remove("Ali")    # Removes first "Ali"
names.append("Noor")
```

### Python Lists
A list in Python is an ordered, mutable (changeable) collection of items. You can store numbers, strings, other lists – even mixed types – all in one list!

**Creating a List:**
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4]
mixed = ["Python", 3.14, True]
```

**Accessing Elements:**
- **By index (starts at 0):**
```python
print(fruits[0])    # "apple"
print(fruits[-1])   # "cherry" (negative index from end)
```

**Changing List Items:**
Lists are mutable – you can change any item:
```python
fruits[1] = "mango"
```

**List Slicing:**
Extract a part of the list:
```python
fruits[0:2]    # ["apple", "mango"]
fruits[::-1]   # Reversed list
```

**Useful List Methods:**
- `append(item)` → adds item to end
- `insert(i, item)` → inserts at index

### Looping Through Lists
```python
for fruit in fruits:
    print(fruit)
```

**Nested Lists:**
Lists can contain other lists:
```python
matrix = [[1, 2], [3, 4]]
print(matrix[0][1])    # 2
```

### Indexing, Adding & Removing Items + Comprehensions

**Indexing:**
Python lists are zero-indexed. This means the first item is at index 0, the second at 1, and so on.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # Output: "apple"
print(fruits[-1])   # Output: "cherry" (last item)
```

Use negative indexing to access elements from the end.

**append():**
Adds a single element to the end of a list.
```python
numbers = [1, 2, 3]
numbers.append(4)    # [1, 2, 3, 4]
```

**insert():**
Inserts an element at a specified index.
```python
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")    # ["apple", "banana", "cherry"]
```

**remove(item)** → deletes first occurrence
**pop(i)** → removes item at index
**sort()** → sorts list (in-place)
**reverse()** → reverses the list
**count(item)** → counts occurrences
**index(item)** → gets first index of item
**clear()** → removes all elements

**Example:**
```python
nums = [4, 2, 8]
nums.append(10)
nums.sort()    # [2, 4, 8, 10]
```

If the item doesn't exist, it raises an error.

**List Comprehension:**
A clean and powerful way to create lists in one line using logic.
```python
squares = [x*x for x in range(5)]
# [0, 1, 4, 9, 16]
even = [x for x in range(10) if x % 2 == 0]    # [0, 2, 4, 6, 8]
```

It's faster and more readable than using a loop for list transformation.

**Bonus: Nested List Comprehension:**
You can even do 2D list generation:
```python
matrix = [[i for i in range(j)] for j in range(3)]
# [[0, 1, 2], [0, 1, 2]]
```

---

## Tuples in Python

### Tuples in Python
A tuple is a built-in data structure that stores an ordered, immutable (unchangeable) collection of values. Think of it like a list you can't modify.

**Defining a Tuple:**
You create a tuple by placing items inside parentheses ():
```python
colors = ("red", "green", "blue")
```
*Even without parentheses, comma-separated values form a tuple:*
```python
example = 1, 2, 3
```

**Accessing Tuple Elements:**
Use indexing just like lists:
```python
print(colors[0])    # Output: "red"
print(colors[-1])   # Output: "blue"
```

**Tuple Characteristics:**
- **Ordered:** Items have a defined order
- **Immutable:** You cannot add, remove, or change items
- **Allow duplicates:** Like lists, tuples can store repeated values
- **Can store mixed data types:** Integers, strings, lists, etc.
- **Ideal for fixed data like coordinates, dates, or settings
- **Faster than lists**
- **Usable as dictionary keys (lists can't be keys)**

**Why Use Tuples?**
- **Faster than lists**
- **Safer when you don't want data to change**
- **Ideal for fixed data like coordinates, dates, or settings**
- **Usable as dictionary keys (lists can't be keys)**

**Tuple Operations:**
```python
t = (1, 2, 3)
len(t)    # 3
3 in t    # True
t * 2     # (1, 2, 3, 1, 2, 3)
t + (4, 5, 3, 2) in t    # (1, 2, 3, 4, 5, 3, 2) in t
```

**Tuple Unpacking:**
You can assign tuple elements to variables directly:
```python
point = (10, 20)
x, y = point
print(x)    # 10
```

### 1. Tuple
The most common immutable collection. Ordered list you can access with square brackets and supports indexing.

### 2. String
Though technically not a collection in the traditional sense, strings behave as immutable sequences of characters.

### 3. Frozenset
An immutable version of a set whose elements are unique, unordered elements and is hashable – can be used as keys or items of another set.

**Why Use Immutable Collections?**
- **Thread-safety** in multi-threaded programs
- **Safer for function arguments**
- **Can be used as dictionary keys**
- **Prevent accidental changes**
- **Useful in multi-threading applications**

**Immutable Collections in Python:**
Immutable means unchangeable after creation. Once created, you cannot add, remove, modify – or altering items.

**Immutability improves data safety, predictability, and performance in memory-critical tasks.**

---

## Python Dictionaries

### Dictionary Methods
A dictionary is a collection of key-value pairs. Keys must be unique and immutable, but values can be of any type.

**Creating a Dictionary:**
```python
student = {"name": "John", "age": 20}
grades = dict(math=95, english=88)
```

**Accessing Values:**
```python
print(student["name"])    # "John"
print(student.get("grade", "Not found"))    # Safe access
```

**Why Multidictionaries:**
- Fast lookups by key
- Keys must be unique and immutable  
- Flexible data structures when working with complex data

**Accessing Values:**
- `dict[key]` - Direct access (raises KeyError if key doesn't exist)
- `dict.get(key, default)` - Safe access with default value

**Updating:**
```python
student["grade"] = "A+"
student.update({"city": "NYC", "major": "CS"})
```

**Adding or Updating:**
```python
student["email"] = "john@email.com"    # Add new key
student["age"] = 21    # Update existing key
```

**Removing/Updating:**
```python
del student["age"]    # Remove key-value pair
removed_value = student.pop("grade")    # Remove and return value
student.clear()    # Remove all items
```

**Key and Values:**
```python
keys = student.keys()
values = student.values()
items = student.items()    # Key-value pairs as tuples
```

**Looping Through Dictionary:**
```python
# Loop through keys
for key in student:
    print(key)

# Loop through values  
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
```

---

## Python Sets

### Membership Tests
A set is an unordered collection of unique elements. Very fast for membership testing and removing duplicates.

**Creating a Set:**
```python
numbers = {1, 2, 3, 4, 5}
colors = set(["red", "green", "blue"])
empty_set = set()    # Note: {} creates an empty dictionary
```

**When to Use Sets:**
- Remove duplicates from a collection
- Fast membership testing (`in` operator)  
- Mathematical set operations (intersection, union, etc.)

**Adding Elements:**
```python
numbers.add(6)
numbers.update([7, 8, 9])    # Add multiple elements
```

**Removing Elements:**
```python
numbers.remove(3)    # Raises KeyError if not found
numbers.discard(10)    # Silent if not found  
popped = numbers.pop()    # Remove arbitrary element
numbers.clear()    # Remove all elements
```

**Set Operations:**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (all elements)
union = set1 | set2    # {1, 2, 3, 4, 5, 6}

# Intersection (common elements)  
intersection = set1 & set2    # {3, 4}

# Difference (elements in set1 but not set2)
difference = set1 - set2    # {1, 2}

# Symmetric Difference (elements in either but not both)
sym_diff = set1 ^ set2    # {1, 2, 5, 6}
```

**Common Set Operations:**
- `len(s)` - Get size
- `x in s` - Check membership
- `s.copy()` - Create a copy
- `s.issubset(other)` - Check if subset
- `s.issuperset(other)` - Check if superset

---

## Useful Built-in Functions

Python provides many built-in functions that work with different data types:

### Sequence Functions
- `len(obj)` - Get length of sequence
- `sum(iterable)` - Sum numeric values  
- `min(iterable)` - Find minimum value
- `max(iterable)` - Find maximum value
- `sorted(iterable)` - Return sorted list
- `reversed(seq)` - Return reversed iterator

### Type Functions  
- `type(obj)` - Get object type
- `isinstance(obj, class)` - Check if object is instance
- `str()`, `int()`, `float()`, `bool()` - Type conversion

### Iteration Functions
- `enumerate(iterable)` - Get index and value pairs
- `zip(iter1, iter2, ...)` - Combine iterables  
- `range(start, stop, step)` - Generate number sequence
- `filter(function, iterable)` - Filter elements
- `map(function, iterable)` - Apply function to elements

### Useful Examples:
```python
# Get index and value
for i, value in enumerate(['a', 'b', 'c']):
    print(f"{i}: {value}")

# Combine lists
names = ["Alice", "Bob"]  
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))

# Square all numbers
squares = list(map(lambda x: x**2, [1, 2, 3, 4]))
```

### Unique Values & Set Operations

**Difference Elements (set1.difference(set2) or set1 - set2):**
Elements present in first set but not in second:
```python  
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a - b)    # {1, 2, 3}
```

**Symmetric Difference (set1 ^ set2):**
Elements in either set but not in both:
```python
print(a ^ b)    # {1, 2, 3, 6, 7, 8}
```

**Union (set1 | set2):**
All unique elements from both sets:
```python
print(a | b)    # {1, 2, 3, 4, 5, 6, 7, 8}
```

**Intersection (set1 & set2):**
Common elements in both sets:
```python
print(a & b)    # {4, 5}
```

**Other Set Methods:**
- `s.add(elem)` - Add single element
- `s.update(iterable)` - Add multiple elements  
- `s.remove(elem)` - Remove element (raises KeyError if not found)
- `s.discard(elem)` - Remove element (silent if not found)
- `s.pop()` - Remove and return arbitrary element
- `s.clear()` - Remove all elements
- `s.copy()` - Create shallow copy

**Set Comparison:**
- `s.isdisjoint(other)` - True if no common elements
- `s.issubset(other)` - True if s is subset of other
- `s.issuperset(other)` - True if s is superset of other

---

*This comprehensive guide covers essential Python programming concepts including operators, I/O, data types, slicing, formatting, dictionaries, sets, and built-in functions for quick reference and study.*
