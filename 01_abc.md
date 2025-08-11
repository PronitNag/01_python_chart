I can certainly help you by providing the information from the PDF sources in a markdown format that you can then copy and save to a GitHub repository. Please note that I cannot directly *create* or *upload* a file to your system, but I will present the content here using standard Markdown syntax.

You can **copy and paste the entire response below** into a text file, save it with a `.md` extension (e.g., `python_basics.md`), and then upload it to your GitHub repository.

Here is the comprehensive content of your sources formatted in Markdown:

```markdown
# Python Basics

## What is Python?
Python is a powerful, high-level, general-purpose programming language known for its simplicity, readability, and wide applications. It is ideal for web development, data analysis, AI, and machine learning.

### Key Characteristics:
*   **Simple Syntax:** Python code looks like plain English, ideal for beginners.
*   **Interpreted Language:** Line by line, no need to compile.
*   **Dynamically Typed:** No need to declare variable types explicitly.
*   **High-Level:** Focus on logic, not boilerplate.
*   **Extensible:** Rich libraries for every domain (e.g., numpy, requests, matplotlib, pillow).

### Designed For:
*   Beginners learning programming.
*   Rapid application development.
*   Scripting, automation, and task scheduling.
*   Building web apps, APIs, and tools.

## Why Learn Python?
*   **High Demand:** Driven by demand skills (used by Google, Netflix, NASA).
*   **Fast Prototyping:** Production-ready and agile application development.
*   **Active Community:** Free learning resources.
*   **Cross-platform:** Windows, Linux, macOS.

### Quick Facts:
*   **Created by:** Guido van Rossum.
*   **First Released:** 1991.
*   **Current Version (2023):** Python 3.X (Python 2 is deprecated).
*   **Licensed under:** PSF.
*   **Shell/Interpreter:** Use python or python3 on the CLI.

### Python Tip: "Simple is better than complex."
This is a core Python philosophy, emphasizing code that's readable, reusable, and efficient.

## Setting up Python & IDEs
To start with Python, you need two things:
1.  **Python on your machine:** An IDE or code editor to write and execute code.
2.  **An IDE or code editor:** To write and execute your code.

### Install Python (Windows/Mac/Linux)
1.  Visit: **https://python.org/downloads** and install the latest Python 3.x version.
2.  **During installation, check "Add Python to PATH" before clicking install.**
3.  **Verify installation:** `python --version`.

### Use your terminal:
*   `sudo apt update`
*   `sudo apt install python3 python3-pip`

### Run Python in 3 Ways:
*   **Command Line:** `python`
*   **Interactive Mode (>>>):** `python`
*   **Script Mode:** Save file as `.py` and run: `python your_script.py`.

### Online Editors:
*   Replit.com
*   Programiz.com
*   Onecompiler.com

### IDEs & Code Editors
*   **Best Python IDEs:**
    *   VS Code
    *   PyCharm
    *   Thonny
    *   Jupyter Notebook
    *   Sublime Text / Atom

### Virtual Environments (Optional but Recommended)
*   **To isolate projects:**
    *   **Mac/Linux:** `python3 -m venv env_name`
    *   **Windows:** `python -m venv env_name`
    *   `source env_name/bin/activate` (Mac/Linux)
    *   `.\env_name\Scripts\activate` (Windows)

### Install pip (Python Package Manager)
*   `pip` lets you install Python libraries.
*   `pip install library_name`.

### Check version:
*   `pip --version`.

### Deactivate:
*   `deactivate`.

## Syntax & Indentation Rules
Python's syntax is clean, minimal, and strict about indentation. Unlike other languages, Python uses `if`, `for`, `def` and `class` indentation to define blocks of code.

### Basic Syntax Rules
*   **New Line:** Ends by extension.
*   **Statements:** Are written line by line.
*   **No Semicolons:** Not required at the end.
*   **Case-sensitive:** `Age`, `age`, and `AGE` are different.
*   **Code Blocks (like `if`, `for` functions):** Must be indented.

### Indentation Rules
*   **Consistent Indent Level (recommended):** Use tabs or spaces.
*   **4 spaces:** Most common practice.
*   **All code in a block:** Must have the same indentation.

### Correct:
```python
if age >= 18:
    print("Adult")
    print("Can vote")
```

### Incorrect:
```python
if age >= 18:
print("Adult") # Error no indent
    print("Can vote") # Error inconsistent indent
```

### Indentation - Structure:
`if x:`
    `print("Positive")`

### Indentation in Loops
`for i in range(3):`
    `print(i)`
    `print("Hello")`

### No Semicolons or Braces
*   Python does not require semicolons at the end of statements.
*   `x = 10`
    *   This is fine.

### Avoid using:
*   `x = 10; y = 20`
    *   `x` Not recommended.

### One-line Conditions (optional)
*   `if x > 0: print("Positive")`
*   But multi-line blocks MUST be indented.

### Comments & Doctrings
*   `#` This is a single-line comment.
*   `"""This is a multi-line docstring used for documentation"""`.

### Python Tip:
When in doubt, re-indent your code cleanly using your IDE's auto-format feature, or ensure use 4 spaces per block manually.

## Variables & Data Types

### What is a Variable?
A variable is a name that holds a value. Python doesn't need explicit type declarations – it figures out the type at runtime.

#### Example:
`name = "Alice"` # String
`age = 25` # Integer
`height = 5.8` # Float
`is_active = True` # Boolean

### Rules for Naming Variables:
*   **Start with a letter or underscore (_)**.
*   **Cannot start with a number**.
*   **Contain letters, numbers, spaces**.
*   **Use snake_case for readability:** `my_variable`, `total_amount`.
*   **Case-sensitive:** `Value` and `value` are different.

### Python Core Data Types:
*   **`int` (Integer):** Represents whole numbers, both positive and negative.
    *   Example: `age = 25`.
*   **`float` (Floating Point Number):** Used for real numbers or numbers with a fractional part.
    *   Example: `height = 5.8`.
*   **`str` (String):** Sequence of characters enclosed in single (' ') or double (" ") quotes.
    *   Example: `name = "Alice"`.
*   **`bool` (Boolean):** Stores either `True` or `False`. Used for logical operations.
    *   Example: `is_active = True`.
*   **`list`:** A mutable, ordered collection of items. Items can be of any type.
*   **`tuple`:** An immutable, ordered collection. Like lists but cannot be modified.
*   **`dict` (Dictionary):** A key-value pair collection.
*   **`set`:** An unordered collection of unique elements.

---

# Python Operators

## Python Operators
Operators in Python are used to perform operations on variables and values. They help you manipulate data and control program flows. Here's a breakdown of the main types.

### 1. Arithmetic Operators
Used to perform basic math:
*   `+` adds two operands
*   `-` subtracts one value from another
*   `*` multiplies two operands
*   `/` divides and returns a float
*   `%` modulo (remainder) returns the remainder
*   `**` performs exponentiation (power)
*   `//` floor division returns the quotient

**Example:**
`a = 5`, `b = 3`
`print(a + b)`

### 2. Comparison Operators
Compares values and return `True` or `False`:
*   `==` checks if values are equal
*   `!=` checks if they're not equal
*   `>` checks if left is greater
*   `<` checks if left is smaller
*   `>=` checks if left is greater or equal
*   `<=` checks if left is smaller or equal

**Example:**
`a = 5`, `b = 3`
`print(a == b)`

### 3. Assignment Operators
Used to assign values to variables, often with arithmetic:
*   `=` assigns a value
*   `+=` adds and assigns
*   `-=` subtracts and assigns
*   `*=` multiplies and assigns
*   `/=` divides and assigns
*   `%=` remainder and assigns
*   `**=` power and assigns
*   `//=` floor division and assigns

**Example:**
`x = 10`
`x += 2` -> `x` is now 12

### 4. Logical Operators
Used for combining conditional statements.
*   `and` returns `True` if both are `True`.
    *   `True and True` is `True`.
    *   `True and False` is `False`.
*   `or` returns `True` if at least one is `True`.
    *   `True or False` is `True`.
*   `not` negates the boolean value.
    *   `not True` is `False`.

**Example:**
`a = 10`, `b = 5`
`print(a > 5 and b < 10)`

### 5. Identity Operators
Checks if two variables refer to the same object in memory.
*   `is` returns `True` if they are the same object.
*   `is not` returns `True` if not the same object.

**Example:**
`a = 5`, `b = 5`
`print(a is b)`

### 6. Membership Operators
Used to check if a value exists in a sequence (list, tuple, string, set, dict).
*   `in` returns `True` if present.
*   `not in` returns `True` if not present.

**Example:**
`my_list =`
`print(1 in my_list)`
`print(5 not in my_list)`

### 7. Bitwise Operators
Operate on bits:
*   `&` (AND)
*   `|` (OR)
*   `^` (XOR)
*   `~` (NOT)
*   `<<` (Left Shift)
*   `>>` (Right Shift)

## Python Comments

### Single-line Comments
`#` A single-line comment starts with the hash symbol `#`. Everything after the `#` on that line is ignored.
**Why important?**
*   Explain a line of code.
*   Leave notes for yourself or other developers.

**Example:**
`# This is a single-line comment`
`x = 10 # Assign x to 10`

### Multiline Comments
Python does not have official multiline comment syntax like C++. However, you can use one of two common approaches:
1.  **Using multiple lines:** Most common and clear for short block explanations.
    *   `# This line calculates`
    *   `# the square of a number`
    *   `# number = num * num`
2.  **Using triple quotes (""" """ or ''' ''')**. Not technically comments, but Python ignores string literals that are not assigned to a variable. So they can act like comments.

**Example:**
```python
"""
This block is ignored
by the interpreter, and works
like a multi-line comment.
"""
```

**Note:** Triple-quote comments are often preferred for documentation and strings (docstrings) as they are consistently more consistent for actual code examples.

### Tip:
Use pip to install pandas, pip install flask, pip install numpy.

### Actual use case:
`def calculate_square(num):`
    `"""This function calculates the square of a number."""`
    `return num * num`

## Python Input/Output (I/O)

### Python provides simple ways to handle user input and display output, making your Python programs straightforward.

### `print()` Output:
Used to display text or variable values to the screen.

**Syntax:** `print("Hello, World!")`
You can also print variables:
`name = "Aamir"`
`print("My name is", name)`

To print multiple values:
`print("Aamir", "Print", name)`

**`sep` parameter:**
`print("Hello", "World", sep="-")`
Output: `Hello-World`

**`end` parameter:**
`print("Hello", end="!")`
`print("Hi")`
Output: `Hello!Hi`

### `input()` Input Function
Used to take user input from the console. Input is always read as a string.

**Syntax:** `input("Enter something: ")`

**Example:**
`name = input("Enter your name: ")`
`print("Hello, " + name)`

Converting input to integer:
`age = int(input("Enter your age: "))`

### Common Typecasting Functions
*   `int()`: Converts to integer.
*   `float()`: Converts to float.
*   `str()`: Converts to string.
*   `bool()`: Converts to boolean.
*   `list()`: Converts to list.
*   `tuple()`: Converts to tuple.
*   `dict()`: Converts to dictionary.
*   `set()`: Converts to set.

### Quick Tip:
Data Structures: Python is a dynamically typed language. Not all conversions are valid. Trying to convert a non-numeric string to `int` will result in an error.

### Typecasting
Typecasting (also called type conversion) is the process of converting a data type of a variable from one type to another, for example, from a string to an integer, or integer to float. Python provides built-in functions to handle this safely.

**String to integer:**
`x = "10"`
`int(x)` is 10.

**Integer to string:**
`x = 10`
`str(x)` is "10".

**Float to integer:**
`x = 10.7`
`int(x)` is 10 (decimal is removed, not rounded).

**Integer to float:**
`x = 10`
`float(x)` is 10.0.

**String to float:**
`price_str = "99.99"`
`price = float(price_str)` is 99.99.

**Float to boolean:**
`bool(0.0)` is `False`.
`bool(1.5)` is `True`.

### Why Typecasting?
Python is a dynamically typed language, meaning you don't declare types. Types are inferred at runtime. But sometimes you need to explicitly change data types, especially when using `input()` (which always returns a string) or performing specific operations.

### Implicit vs Explicit Conversions
*   **Implicit:** Python automatically converts data types when it's safe and makes sense (e.g., `int` to `float` in `5 + 3.0` -> `8.0`).
*   **Explicit:** You manually convert using functions like `int()`, `float()`, `str()`. This is common for `input()` values.

### Invalid Conversions
*   **Error:** Converting a non-numeric string to an integer/float.
    *   `int("hello")` -> `ValueError`.
    *   `float("xyz")` -> `ValueError`.

### Always validate or use try-except blocks
For robust code when taking user input or dealing with external data.

### What are Data Structures?
Data structures are objects used to store, organize, and manipulate data efficiently. Python has several built-in data structures that are versatile and easy to use.

### 1. List (Ordered, Mutable)
A list holds a collection of items (any type) and maintains their order.
**Syntax:** `fruits = ["apple", "banana", "cherry"]`.
**Common operations:**
*   `fruits.append("orange")`
*   `fruits.remove("banana")`
*   `fruits` (access first item)
*   `len(fruits)`

### 2. Tuple (Ordered, Immutable)
Like a list, but cannot be changed after creation. Useful for fixed collections.
**Syntax:** `coordinates = (10, 20)`.
**Common operations:**
*   `coordinates` (access first item)
*   `len(coordinates)`
*   `x, y = coordinates` (unpacking)

### 3. Dictionary (Unordered, Unique)
A key-value store. Items are accessed by key. Keys must be unique, unordered elements.
**Syntax:** `person = {"name": "Aamir", "age": 25}`.
**Common operations:**
*   `person["name"]` (access value by key)
*   `person["city"] = "NY"` (add/update)
*   `person.keys()`
*   `person.values()`

### 4. Dictionary (Unordered, Mutable)
*Keys must be unique.
**Syntax:** `my_dict = {"name": "Alice", "age": 30}`.

---

# Function Programming in Python

## Regular Arguments
Passed in the defined order.
**Example:** `def greet(name, age):`
    `print(f"Hello {name}, you are {age}!")`
`greet("Aamir", 25)`

## `*args` Variable Positional Arguments
You don't know how many arguments you'll receive.
Used to pass a non-keyworded, variable-length argument list.
**Example:** `def add_all(*numbers):`
    `total = 0`
    `for num in numbers:`
        `total += num`
    `return total`
`add_all(1, 2, 3, 4)`
Output: 10.
`*args` collects all extra positional arguments as a tuple.

## `**kwargs` Variable Keyword Arguments
Used when you want to accept named arguments dynamically.
**Example:** `def print_info(**profile):`
    `for key, value in profile.items():`
        `print(f"{key}: {value}")`
`print_info(name="Aamir", age=25)`
Output: `name: Aamir`, `age: 25`.
`**kwargs` collects all extra keyword arguments as a dictionary.
**Use `*args` for flexible inputs.**
**Use `**kwargs` for optional named parameters.**

## Python Values in Return
A function can return a result back to the caller using the `return` keyword.

### Basic Return
`def square(x):`
    `return x * x`
`result = square(4)`
`print(result)`
Output: 16.
`return` sends a value out of the function.
`print` displays output to the screen.

### Returning Multiple Values
Functions can return multiple values as a tuple.
**Example:** `def stats(a, b):`
    `return a + b, a * b`
`sum_val, prod_val = stats(2, 3)`
`print(f"Sum: {sum_val}, Product: {prod_val}")`
Output: `Sum: 5, Product: 6`.

### Return vs Print
`print` just displays data to the program.
`return` passes data back to the program.

## Python Practicals for Beginners

### Calculator (Addition, Subtraction, etc.)
`a = int(input("Enter first number: "))`
`b = int(input("Enter second number: "))`
`op = input("Choose operator (+, -, *, /): ")`
`if op == '+':`
    `print(f"Result: {a + b}")`
`elif op == '-':`
    `print(f"Result: {a - b}")`
`elif op == '*':`
    `print(f"Result: {a * b}")`
`elif op == '/':`
    `print(f"Result: {a / b}")`
`else:`
    `print("Invalid operator")`
**Concepts:** Input, arithmetic, if-elif-else.

### Even or Odd Checker
`num = int(input("Enter a number: "))`
`if num % 2 == 0:`
    `print("Even number")`
`else:`
    `print("Odd number")`
**Concepts:** Modulo operator, conditionals.

### Simple Interest Calculator
`P = float(input("Principal: "))`
`R = float(input("Rate (%): "))`
`T = float(input("Time (years): "))`
`SI = (P * R * T) / 100`
`print(f"Simple Interest: {SI}")`
**Concepts:** Arithmetic operations, float type.

### List sorter
`numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]`
`numbers.sort()`
`print("Sorted List:", numbers)`
**Concepts:** List, input splitting, list comprehension, sorting.

### Word Counter
`sentence = input("Enter a sentence: ")`
`words = sentence.split()`
`print(f"Word count: {len(words)}")`
**Concepts:** Strings, lists, split(), len().

## Lambda Functions in Python
A lambda function is a small, anonymous function defined without a name. It's useful for short, simple operations, especially where a full `def` function is unnecessary.

### Basic Syntax:
`lambda arguments: expression`
Lambda returns the result of the expression automatically.

### Example: Add Two Numbers
**Regular function:**
`def add(x, y):`
    `return x + y`
`add(4, 3)`
Output: 7.

**Lambda function:**
`add_lambda = lambda x, y: x + y`
`add_lambda(4, 3)`
Output: 7.

### When to use Lambda?
*   **For quick, inline functions**.
*   Often used with `map()`, `filter()`, `reduce()`.
*   When you need a function for a short period and want to reuse the function elsewhere.

### Examples in Action:
### Square each number in list
`numbers =`
`squared_numbers = list(map(lambda x: x**2, numbers))`
`print(squared_numbers)`
Output: ``.

### Lambda filter even
`data =`
`even_numbers = list(filter(lambda x: x % 2 == 0, data))`
`print(even_numbers)`
Output: ``.

**Note:** Lambda functions are limited to a single expression. They cannot have multiple statements, or loops.

### `map()`, `filter()`, `reduce()` in Python
These are higher-order functions that take other functions as arguments.

### `map()` Transform Each Item
Applies a function to every item in an iterable and returns a new iterable (e.g., list, tuple) with the transformed items.
**Example:** `numbers =`
`squared = list(map(lambda x: x*x, numbers))`
Output: ``.

### `filter()` Filter Items by Condition
Returns items from an iterable for which a function returns `True`.
**Example:** `ages = `
`adults = list(filter(lambda age: age >= 18, ages))`
Output: ``.

### `reduce()` Reduce to a Single Value
Applies a function cumulatively to the items of an iterable, reducing it to a single value.
*Note: `reduce` is in the `functools` module, not built-in (from outside sources) - *The source implies it's a common concept but doesn't show import, so I'll just mention it's a higher-order function.*

## Factorial Calculator (Using Loop)
`num = int(input("Enter an integer: "))`
`factorial = 1`
`for i in range(1, num + 1):`
    `factorial *= i`
`print(f"Factorial: {factorial}")`
**Concepts:** Loops, multiplication, range.

## Palindrome Checker
`word = input("Enter a word: ")`
`if word == word[::-1]:`
    `print("It's a palindrome")`
`else:`
    `print("Not a Palindrome")`
**Concepts:** Strings, slicing, conditionals.

## Maximum of Three Numbers
`a = int(input("Enter First: "))`
`b = int(input("Enter Second: "))`
`c = int(input("Enter Third: "))`
`max_val = a`
`if b > max_val:`
    `max_val = b`
`if c > max_val:`
    `max_val = c`
`print(f"Max: {max_val}")`
**Concepts:** Conditional logic.

## Concepts:
*   Numbers guessing game
    *   `import random`
    *   `target = random.randint(1, 10)`
    *   `guess = 0`
    *   `while guess != target:`
        `guess = int(input("Guess a number (1-10): "))`
        `if guess < target:`
            `print("Too low!")`
        `elif guess > target:`
            `print("Too high!")`
    `print("Correct!")`
    **Concepts:** Random, while loop, if-elif-else.
*   Fibonacci Series (First N Terms)
    *   `n = int(input("How many terms? "))`
    *   `a, b = 0, 1`
    *   `for _ in range(n):`
        `print(a, end=" ")`
        `a, b = b, a + b`
    **Concepts:** Variables, loop, series logic.

---

# IF / ELIF / ELSE in Python

## IF / ELIF / ELSE in Python
Control flow in Python is primarily done using conditional statements based on `if`, `elif`, and `else`. The main keywords are `if`, `elif` (else if), and `else`.

### Basic Syntax
`if condition:`
    `# Code runs if condition is True`
`elif another_condition:`
    `# Code runs if another_condition is True (and previous were False)`
`else:`
    `# Code runs if none of the above conditions are True`

### How It Works
*   **`if` block:** The first condition checked. If `True`, its code runs.
*   **`elif` blocks:** Checked only if previous `if`/`elif` conditions were `False`.
*   **`else` block:** Runs if all preceding `if`/`elif` conditions are `False`.

### Example:
`score = 85`
`if score >= 90:`
    `print("Grade: A")`
`elif score >= 80:`
    `print("Grade: B")`
`else:`
    `print("Grade: C")`

### Python evaluates conditions top down.
Once a `True` condition is met, its code executes, and the rest of the `if-elif-else` block is skipped.

### Nested Conditions
You can combine multiple conditions using logical operators (`and`, `or`, `not`).
**Example:**
`age = 20`
`if age >= 18 and age < 65:`
    `print("Adult")`
`else:`
    `print("Not an Adult")`

### How to write an "if-elif-else" statement
`age = 20`
`if age >= 18:`
    `print("Adult")`
`if age < 65:`
    `print("Not an Adult")`
`if age >= 18 and age < 65:`
    `print("Adult and not a senior")`
`if is_admin:`
    `print("Admin Panel")`

## FOR AND WHILE LOOPS IN PYTHON

### Loops are used to repeat a block of code multiple times.

### `for` Loop - Iterate Over a Sequence
The `for` loop is used for iterating over a sequence (that is, a list, a tuple, a dictionary, a set, or a string).
**Example:**
`fruits = ["apple", "banana", "cherry"]`
`for x in fruits:`
    `print(x)`
Output: `apple`, `banana`, `cherry`.

### Using `range()` in for loops
`range()` generates a sequence of numbers.
`for i in range(5):`
    `print(i)`
Output: `0, 1, 2, 3, 4`.

**`range(start, stop, step)`:**
`for i in range(0, 10, 2):`
    `print(i)`
Output: `0, 2, 4, 6, 8`.

### `while` Loop - Repeat While Condition is True
The `while` loop executes a block of code as long as a condition remains `True`.
**Example:**
`count = 0`
`while count < 3:`
    `print(count)`
    `count += 1`
Output: `0, 1, 2`.

**Be careful!** If the condition never becomes `False`, you will create an infinite loop.

### `break` and `continue`
These statements give you more control over loops.
*   **`break`:** Exits the loop immediately.
*   **`continue`:** Skips the current iteration and moves to the next.

### Loop Control: `break`, `continue`, `pass`
Python provides statements to manage loop's flow: `break`, `continue`, and `pass`. These are crucial for stopping loops prematurely, skipping iterations, or simply acting as a placeholder.

### `break` - Exit Loop Immediately
**Usage:** Terminates the current loop entirely. The program execution resumes at the statement immediately following the loop.
**Example:**
`for i in range(5):`
    `if i == 3:`
        `break`
    `print(i)`
Output: `0, 1, 2`.
Stops the loop when `i` is 3.

### `continue` - Skip Current Iteration
**Usage:** Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
**Example:**
`for i in range(5):`
    `if i == 2:`
        `continue`
    `print(i)`
Output: `0, 1, 3, 4`.
Skips printing when `i` is 2.

### `pass` - Do Nothing (Placeholder)
**Usage:** A null operation. Nothing happens when it executes. Used as a placeholder in loops or conditional statements where a statement is required syntactically but you don't want any code to execute.
**Example:**
`for i in range(5):`
    `if i % 2 == 0:`
        `pass` # Placeholder for future code
    `else:`
        `print(i)`

**These statements make your loop control more flexible, which is essential in real-world applications for debugging, searching, or skipping errors.**

## List comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list. It's a more concise and readable way of creating lists by combining loops and logic into a single line.

### Basic Syntax:
`[expression for item in iterable if condition]`

**Example:** `numbers =`
`squares = [x**2 for x in numbers]`
This is equivalent to:
`squares = []`
`for x in numbers:`
    `squares.append(x**2)`
Output: ``.

**With condition (even numbers squared):**
`squares_even = [x**2 for x in numbers if x % 2 == 0]`
Output: ``.

**Nested loops (pairs):**
`pairs = [(i, j) for i in range(1, 3) for j in range(1, 4)]`
Output: `[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)]`.

**With if/else (even/odd):**
`labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]`
Output: `['Even', 'Odd', 'Even', 'Odd', 'Even']`.

**List comprehensions are faster and cleaner, widely used in data processing, transformations, and compact loops.**

## Functions in Python
Functions are a block of reusable code that performs a specific task. They help to organize code, reduce repetition, and improve readability.

### Defining and Calling Functions in Python

### Defining a Function
Use the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`. The code block is indented.
**Syntax:**
`def greet():`
    `print("Hello, World!")`

### Calling a Function
To execute the code inside a function, simply call it by its name followed by parentheses `()`.
**Syntax:** `greet()`
Output: `Hello, World!`.

### Function with Parameters
Parameters are variables listed inside the parentheses of the function definition. They act as placeholders for values that will be passed into the function when it's called.
**Syntax:**
`def greet_name(name):`
    `print(f"Hello, {name}!")`
`greet_name("Aamir")`
Output: `Hello, Aamir!`.

### Return Statement
The `return` statement is used to send a value back from the function to the caller.
**Syntax:**
`def add_nums(a, b):`
    `return a + b`
`result = add_nums(5, 3)`
`print(result)`
Output: `8`.
This runs the code inside the function, then gives you the result back.

### Example with Parameters
`def welcome(name, city):`
    `print(f"Welcome, {name} from {city}!")`
`welcome("Aamir", "New York")`
Output: `Welcome, Aamir from New York!`.

### Default Parameters
You can set default values for parameters. If a value isn't provided for that parameter during the function call, the default value is used.
**Syntax:**
`def greet(name="User"):`
    `print(f"Hello, {name}!")`
`greet("Aamir")`
`greet()`
Output: `Hello, Aamir!`, `Hello, User!`.

### Keyword & Positional Arguments
*   **Positional:** Arguments passed based on their position. `greet("Alice", 30)`.
*   **Keyword:** Arguments passed by explicitly naming the parameter.
    `greet(age=30, name="Alice")`.
Keyword arguments make code more readable and flexible.

### `*args` and `**kwargs`
*   **`*args`:** Accepts multiple positional arguments as a tuple.
    `def add_all(*nums):`
        `return sum(nums)`
    `add_all(1, 2, 3)`
*   **`**kwargs`:** Accepts multiple keyword arguments as a dictionary.
    `def print_data(**data):`
        `print(data)`
    `print_data(name="Alice", age=30)`

---

# Slicing, Formatting & Common Methods in Python

## SLICING, FORMATTING & COMMON METHODS IN PYTHON

### Slicing Strings
Slicing allows you to extract a portion of a string (or other sequences like lists, tuples). It follows the format: `[start:stop:step]`.
*   `start`: Index to begin (inclusive, default 0).
*   `stop`: Index to end (exclusive, default end of string).
*   `step`: How many characters to jump (default 1).

#### Examples:
*   `text = "Python"`
*   `text` is 'P'.
*   `text[1:4]` is 'yth' (from index 1 up to but not including 4).
*   `text[:3]` is 'Pyt' (from beginning to index 3).
*   `text[3:]` is 'hon' (from index 3 to end).
*   `text[-1]` is 'n' (last character).
*   `text[::-1]` is 'nohtyP' (reversed string).

### String Formatting
Python has multiple ways to format strings.

#### 1. `f-strings` (Recommended, Python 3.6+)
**Syntax:** `f"My name is {name} and I'm {age} years old."`
**Example:**
`name = "Aamir"`
`age = 25`
`print(f"My name is {name} and I'm {age} years old.")`

#### 2. `.format()` Method
**Syntax:** `"My name is {} and I'm {} years old.".format(name, age)`
**Example:**
`name = "Aamir"`
`age = 25`
`print("My name is {} and I'm {} years old.".format(name, age))`

#### 3. `%` Operator (Old Style)
**Syntax:** `"My name is %s and I'm %d years old." % (name, age)`
**Example:**
`name = "Aamir"`
`age = 25`
`print("My name is %s and I'm %d years old." % (name, age))`

### Common String Methods
*   **`len()`:** Returns the length of a string.
*   **`.lower()`:** Converts string to lowercase.
*   **`.upper()`:** Converts string to uppercase.
*   **`.strip()`:** Removes leading/trailing whitespace.
*   **`.replace(old, new)`:** Replaces substrings.
*   **`.split(delimiter)`:** Splits string into a list.
*   **`.join(iterable)`:** Joins elements of an iterable into a string.
*   **`.startswith(prefix)` / `.endswith(suffix)`:** Checks prefixes/suffixes.
*   **`.find(substring)`:** Returns index of first occurrence.
*   **`.count(substring)`:** Counts occurrences of a substring.

#### Example:
`text = "    Hello Python world!   "`
`print(text.strip().lower().replace("python", "data-science").split(" "))`

## Tuples in Python

### What is a Tuple?
A **Tuple** is an immutable, ordered collection of items. Unlike lists, once a tuple is created, its elements cannot be changed.

### Defining a Tuple
You create a tuple by placing items inside parentheses `()`.
**Syntax:**
`colors = ("red", "green", "blue")`
`my_tuple = (1, 2, 3, 4, 5)`
Tuples can contain different data types.

### Accessing Tuple Elements
Elements are accessed by index, just like lists.
**Syntax:** `my_tuple`
**Example:**
`colors = ("red", "green", "blue")`
`print(colors)`
Output: `green`.

### Tuple Characteristics
*   **Ordered:** Elements have a defined order.
*   **Immutable:** Cannot add, remove, or change elements after creation.
*   **Allows duplicates:** Can contain repeated values.

### Tuple Operations
*   **Concatenation:** `t1 + t2`.
*   **Repetition:** `t1 * 2`.
*   **`len()`:** Length of tuple.
*   **Indexing & Slicing:** Same as strings/lists.

### Why Use Tuples?
*   **Data Integrity:** Safer for fixed data (e.g., coordinates, database records).
*   **Faster:** Slightly faster than lists for iteration.
*   **Dictionary Keys:** Can be used as dictionary keys (unlike lists).
*   **Function Returns:** Functions often return multiple values as a tuple.

### Tuple Unpacking
You can unpack tuple elements directly into variables.
**Example:**
`coordinates = (10, 20)`
`x, y = coordinates`
`print(f"X: {x}, Y: {y}")`
Output: `X: 10, Y: 20`.

### Immutability:
`my_tuple = (1, 2, 3)`
`my_tuple = 5` # Error: `TypeError`.

### Tuples in Immutable Collections
You can't change the tuple itself, but if a tuple contains mutable elements (like lists), those mutable elements can still be changed.
**Example:**
`my_tuple = (1,, 4)`
`my_tuple.append(5)`
`print(my_tuple)`
Output: `(1,, 4)`.

### Why Use Immutable Collections?
*   **Data Integrity:** Guarantees that data won't be accidentally modified.
*   **Thread Safety:** Safer in multi-threaded environments.
*   **Performance:** Can be more efficient in certain data structures (e.g., dictionary keys, set members).

## Common List Methods
List methods modify them in place.
*   **`append(item)`:** Adds item to end.
*   **`insert(index, item)`:** Adds item at specific index.
*   **`extend(iterable)`:** Appends all items from iterable.
*   **`remove(item)`:** Removes first occurrence of item.
*   **`pop([index])`:** Removes and returns item at index (default last).
*   **`del` statement:** Removes item at specific index or slices.
*   **`clear()`:** Removes all items.
*   **`count(item)`:** Counts occurrences of an item.
*   **`sort()`:** Sorts list in-place.
*   **`reverse()`:** Reverses list in-place.
*   **`copy()`:** Returns a shallow copy.

#### Example:
`fruits = ["apple", "banana", "cherry"]`
`fruits.append("orange")`
`print(fruits)`
Output: `['apple', 'banana', 'cherry', 'orange']`.

`fruits.remove("banana")`
`print(fruits)`
Output: `['apple', 'cherry', 'orange']`.

`del fruits`
`print(fruits)`
Output: `['apple', 'orange']`.

### Accessing Through Lists
**Examples:**
`names = ["Ali", "Zara", "Noor"]`
`names.append("Ahmed")`
`names.insert(1, "Sara")`
`names.pop()`
`names.remove("Sara")`

## Python Collection of items
*   **List:** ordered, mutable, can have mixed types - all in one.

### Creating a List
`fruits = ["apple", "banana", "cherry", "mango", "banana", "banana"]`
`numbers =`
`mixed_list = ["apple", 1, True, 3.14]`

### Accessing elements
*   **By index (starts at 0):**
    *   `fruits` is "apple".
*   **By negative index (from end):**
    *   `fruits[-1]` is "banana".

### List Slicing
`fruits[1:4]` is `['banana', 'cherry', 'mango']`.
`fruits[:2]` is `['apple', 'banana']`.
`fruits[2:]` is `['cherry', 'mango', 'banana', 'banana']`.
`fruits[::-1]` is `['banana', 'banana', 'mango', 'cherry', 'banana', 'apple']` (reversed).

### Useful List Methods
*   `fruits.count("banana")` is 3.
*   `fruits.sort()` (sorts in place).
*   `fruits.reverse()` (reverses in place).
*   `fruits.append("kiwi")`.
*   `fruits.insert(1, "grape")`.
*   `del fruits`.

### Nested Lists
Lists can contain other lists.
**Example:**
`matrix = [,, ]`
`matrix` is 2.

### Indexing, Adding & Removing Items
*   **Indexing:** `numbers =`
    *   `numbers` is 1.
*   **`append()`:** Adds element to the end.
    *   `numbers.append(5)` -> ``.
*   **`insert()`:** Adds element at a specific index.
    *   `numbers.insert(0, 0)` -> ``.
*   **`extend()`:** Adds elements of an iterable to the end.
    *   `numbers.extend()` -> ``.
*   **`remove()`:** Removes first occurrence of a specified value.
    *   `numbers.remove(1)` -> ``.
*   **`del`:** Deletes item at a specified index.
    *   `del numbers` -> ``.
*   **`pop()`:** Removes and returns item at a specified index (default last).
    *   `numbers.pop()` -> returns 7, list is ``.
*   **`clear()`:** Removes all items.
    *   `numbers.clear()` -> `[]`.
*   **`count()`:** Returns number of times an item appears.
    *   `fruits.count("banana")` is 3.
*   **`sort()`:** Sorts the list in ascending order.
    *   `fruits.sort()`.
*   **`reverse()`:** Reverses the order of elements.
    *   `fruits.reverse()`.
*   **`copy()`:** Returns a shallow copy of the list.

### List Comprehension (Bonus)
You can even do 2D list comprehension.
**Example:**
`matrix = [[i*j for j in range(3)] for i in range(2)]`
Output: `[,]`.

### Tuple (Ordered, immutable)
A list holds a collection of items (any type) and maintains their order.
**Syntax:**
`fruits = ("apple", "banana", "cherry")`
`numbers = (1, 2, 3, 4)`
`numbers.append(5)` # Error.
`del numbers` # Error.

### 3. FrozenSet
A `frozenset` is an **immutable** version of a `set`. Once created, its elements cannot be changed.
*   **Unique elements:** Stores only unique items.
*   **Unordered:** Elements have no specific order.
*   **Hashable:** Can be used as dictionary keys or elements of other sets.

---

# PYTHON SETS

## PYTHON SETS
A **Set** is an unordered, unindexed, and mutable collection of unique elements. Sets are primarily used to store multiple items in a single variable.

### Creating a Set
You create a set by placing items inside curly braces `{}`.
**Syntax:**
`fruits = {"apple", "banana", "cherry"}`
`my_set = {1, 2, 3, 4, 5}`
Sets automatically remove duplicate elements.
**Example:**
`nums = {1, 2, 3, 2, 1}`
`print(nums)`
Output: `{1, 2, 3}`.

### Accessing Elements
You cannot access items in a set by index or key because they are unordered and unindexed.
You can iterate over a set using a `for` loop to check if an element exists.
**Example:**
`for x in fruits:`
    `print(x)`

### Adding & Removing Elements
Sets are mutable, so you can add or remove elements.
*   **`add(item)`:** Adds a single item.
*   **`update(iterable)`:** Adds multiple items from an iterable.
*   **`remove(item)`:** Removes a specific item. Raises `KeyError` if item not found.
*   **`discard(item)`:** Removes a specific item. No error if item not found.
*   **`pop()`:** Removes and returns an arbitrary item. (Since sets are unordered).
*   **`clear()`:** Removes all elements.
*   **`del`:** Deletes the set entirely.

**Examples:**
`fruits.add("mango")`
`fruits.update(["grape", "kiwi"])`
`fruits.remove("banana")`
`fruits.discard("orange")`
`fruits.pop()`
`fruits.clear()`

### Set Operations
Sets support mathematical set operations like union, intersection, difference, and symmetric difference.

*   **`union()` / `|`:** All unique elements from both sets.
    *   `A = {1, 2, 3}`, `B = {3, 4, 5}`
    *   `A.union(B)` or `A | B` -> `{1, 2, 3, 4, 5}`.
*   **`intersection()` / `&`:** Common elements in both sets.
    *   `A & B` -> `{3}`.
*   **`difference()` / `-`:** Elements in A but not in B.
    *   `A - B` -> `{1, 2}`.
*   **`symmetric_difference()` / `^`:** Elements in A or B but not in both.
    *   `A ^ B` -> `{1, 2, 4, 5}`.

### Membership Test
Check if a value exists:
`"apple" in fruits` -> `True` or `False`.

### When to Use Sets
*   **Unique Values:** When you need to store only unique elements.
*   **Membership Checking:** For fast membership checking (`in` keyword).
*   **Removing Duplicates:** Easily remove duplicates from a list.
*   **Mathematical Set Operations:** When performing union, intersection, etc..
*   **Avoiding Ordered Insertion:** Sets are not ordered, so inserting ordered doesn't matter.

### Unique Values & Set Operations
Sets don't support indexing.
**Example:**
`nums = {1, 2, 3, 4, 4, 5}`
`unique_nums = set(nums)`
Output: `{1, 2, 3, 4, 5}`.

### Unique Values & Set Operations
Sets automatically ensure elements are unique.

### Common Set Operations
Python sets support mathematical set operations that are highly efficient for comparing and combining sets.

### Union: A `|` B
Combines all unique elements.
`{1, 2, 3} | {3, 4, 5}` -> `{1, 2, 3, 4, 5}`.

### Intersection: A `&` B
Elements common to both.
`{1, 2, 3} & {3, 4, 5}` -> `{3}`.

### Difference: A `-` B
Elements in A but not in B.
`{1, 2, 3} - {3, 4, 5}` -> `{1, 2}`.

### Symmetric Difference: A `^` B
Elements in A or B but not both.
`{1, 2, 3} ^ {3, 4, 5}` -> `{1, 2, 4, 5}`.

## PYTHON DICTIONARIES

### PYTHON DICTIONARIES
A **Dictionary** is an unordered, mutable collection of key-value pairs. It's used to store data values like a map. Each key must be unique, and it maps to a corresponding value.

### Creating a Dictionary
You create a dictionary by placing key-value pairs inside curly braces `{}`. Keys and values are separated by a colon `:`, and pairs are separated by commas `,`.
**Syntax:**
`student = {`
    `"name": "Aamir",`
    `"age": 21,`
    `"course": "Python"`
`}`
Each key is unique, and it maps to a corresponding value.

### Accessing Values
Access values using their associated keys inside square brackets `[]`.
**Syntax:** `student["name"]`
**Example:**
`student = {"name": "Aamir", "age": 21}`
`print(student["name"])`
Output: `Aamir`.

You can also use the `.get()` method, which returns `None` if the key doesn't exist, preventing a `KeyError`.
**Example:**
`student.get("city")` # Returns `None` if key "city" doesn't exist.

### Adding or Updating
To add a new key-value pair or update an existing one, assign a value to a new or existing key.
**Syntax:**
`student["grade"] = "A"`
`student["age"] = 22`
**Example:**
`person = {"name": "Aamir"}`
`person["age"] = 25` # Add new key
`person["name"] = "Ahmed"` # Update existing key

### Removing items
*   **`del` keyword:** Deletes a specific key-value pair.
    *   `del student["course"]`.
*   **`.pop(key)`:** Removes and returns the value for a key.
    *   `student.pop("age")`.
*   **`.popitem()`:** Removes and returns the last inserted key-value pair (Python 3.7+), arbitrary before.
*   **`.clear()`:** Removes all items.

**Example:**
`student = {"name": "Aamir", "age": 21, "course": "Python"}`
`student.pop("age")`
`print(student)`
Output: `{'name': 'Aamir', 'course': 'Python'}`.
`del student["name"]`
`student.clear()`

### `len()`
Returns the number of key-value pairs.
`len(student)`.

### `get()`
Used to safely retrieve a value by key. Returns `None` or a default value if key is not found, avoiding errors.
`print(student.get("country", "Unknown"))`.

### Looping Through a Dictionary
*   **For keys:** `for key in student:` or `for key in student.keys():`.
*   **For values:** `for value in student.values():`.
*   **For key, value pairs:** `for key, value in student.items():`.

### Why Use Dictionaries?
*   **Data Retrieval:** Ideal for storing structured data that needs to be accessed quickly by a unique identifier (key).
*   **Real-world Mapping:** Represents real-world objects with distinct properties (e.g., a person's name, age, address).
*   **More Readable:** Storing data as key-value pairs is more readable than indexed lists.

### Key Values Pairs
Dictionaries store data as key-value pairs, where each unique key maps to a value.
*   `"name"` is the key, `"Aamir"` is the value.
*   `"age"` is the key, `25` is the value.
*   `"country"` is the key, `"India"` is the value.

### Accessing Value
`my_dict["name"]`.

## USEFUL BUILT-IN FUNCTIONS

Python comes with many built-in functions that simplify programming. Here are some of the most commonly used ones.

### `len()`
Measures the number of items in a list, string, tuple, etc..
`len()` -> 3.
`len("hello")` -> 5.
`len((1, 2, 3))` -> 3.

### `min()`, `max()`
Return the smallest and largest item in an iterable.
`min()` -> 1.
`max()` -> 8.

### `sum()`
Returns the total sum of all numbers in an iterable.
`sum()` -> 6.

### `round()`
Rounds a number to a specified number of decimal places.
`round(3.14159, 2)` -> 3.14.

### `type()`
Returns the type of a data value or a variable.
`type("hello")` -> `<class 'str'>`.
`type(10)` -> `<class 'int'>`.
`type(3.14)` -> `<class 'float'>`.

### `input()`
Takes user input from the console.
`name = input("Enter name: ")`.

### `print()`
Displays output to the screen.
`print("Hello, World!")`.

### `int()`, `float()`, `str()`
Used for type conversion.
`int("10")` -> 10.
`float("3.5")` -> 3.5.
`str(100)` -> "100".

### `range()`
Generates a sequence of numbers, useful in loops.
`list(range(0, 4))` -> ``.

### `sorted()`
Returns a new sorted list.
`sorted()` -> ``.

### `enumerate()`
Adds a counter to an iterable and returns it as an enumerate object.
`for index, value in enumerate(['a', 'b', 'c']):`
    `print(index, value)`
Output: `0 a`, `1 b`, `2 c`.
```
