# Python Programming Quick Study Guide

## Setting up Python & IDEs

### Python Installation
- Download Python from python.org
- Install Python with pip package manager
- Set up PATH environment variables
- Verify installation with `python --version`

### IDE Options
- **PyCharm** - Professional IDE with debugging, code completion
- **VS Code** - Lightweight editor with Python extensions
- **IDLE** - Built-in Python IDE
- **Jupyter Notebook** - Interactive development environment
- **Sublime Text** - Fast text editor with Python support

## Basic Syntax

### Variables & Data Types
```python
# Variable assignment
name = "John"
age = 25
height = 5.9
is_student = True

# Data types
int_var = 42        # Integer
float_var = 3.14    # Float
string_var = "text" # String
bool_var = True     # Boolean
list_var = [1,2,3]  # List
```

### Print Statements
```python
print("Hello World")
print(f"Name: {name}, Age: {age}")
print("Value:", variable)
```

### Comments
```python
# Single line comment
"""
Multi-line comment
or docstring
"""
```

## Python Basics

### What is Python?
- High-level, interpreted programming language
- Created by Guido van Rossum
- Known for readable syntax and versatility
- Used for web development, data science, automation, AI

### Key Features
- **Simple syntax** - Easy to learn and read
- **Interpreted** - No compilation needed
- **Cross-platform** - Runs on Windows, Mac, Linux
- **Large ecosystem** - Extensive library support
- **Object-oriented** - Supports OOP principles

### Quick Facts
- File extension: `.py`
- Case-sensitive language
- Uses indentation for code blocks
- Dynamically typed
- Interactive shell available

## Syntax & Indentation Rules

### Indentation Guidelines
- Python uses **indentation** instead of braces `{}`
- Standard indentation: **4 spaces**
- Must be consistent throughout code
- Mixing tabs and spaces causes errors

### Code Structure Example
```python
if condition:
    # 4 spaces indentation
    statement1
    statement2
    if nested_condition:
        # 8 spaces for nested blocks
        nested_statement
else:
    # Back to 4 spaces
    else_statement
```

### Best Practices
- Use 4 spaces (not tabs)
- Be consistent with indentation
- Avoid mixing spaces and tabs
- Use meaningful variable names
- Follow PEP 8 style guidelines

## Variables & Data Types

### Variable Rules
- Must start with letter or underscore
- Can contain letters, numbers, underscores
- Case-sensitive (`age` ≠ `Age`)
- Cannot use Python keywords

### Naming Conventions
```python
# Good variable names
user_name = "John"
total_count = 100
is_valid = True

# Avoid these
x = "John"        # Not descriptive
2name = "Invalid" # Starts with number
class = "Invalid" # Python keyword
```

### Data Type Examples
```python
# Numeric types
integer = 42
floating = 3.14159
complex_num = 2 + 3j

# Text type
text = "Hello Python"
multiline = """This is a
multi-line string"""

# Boolean type
is_true = True
is_false = False

# Collection types
my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3, 4)
my_dict = {"name": "John", "age": 25}
my_set = {1, 2, 3, 4}
```

### Type Checking
```python
type(variable)      # Returns type
isinstance(var, int) # Check if variable is int
```

---

*Updated 2025 Edition - Python Programming Study Guide*
