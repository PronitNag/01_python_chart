# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

grades = {"Nora": 86, "Gino": 55}

# Get a value.
print(grades["Nora"])
print(grades["Gino"])

# Get the number of key-value pairs.
print(len(grades))

# Add a new key-value pair.
grades["Alexander"] = 34
print(grades)
print(len(grades))

# Update a key-value pair.
grades["Gino"] = 78
print(grades)

# Remove a key-value pair.
del grades["Nora"]
print(grades)

# Get the sequence of key-value pairs, keys and values.
print(grades.items())
print(grades.keys())
print(grades.values())

# Update a dictionary with another dictionary.
grades.update({"Nora": 26, "Jack": 19})
