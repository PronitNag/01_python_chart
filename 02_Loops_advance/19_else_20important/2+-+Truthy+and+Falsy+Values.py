# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

# Falsy
print(bool(None))
print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(""))
print(bool(0))
print(bool(0.0))

# Truthy
print(bool([1, 2, 3]))
print(bool((1, 2, 3)))
print(bool({1, 2, 3}))
print(bool({"a": 1, "b": 2}))
print(bool(5))
print(bool(8.7))
print(bool(True))
print(bool("Python"))

# Loops
my_list = [1, 2, 3, 4]

while my_list:
    my_list.pop()
    print(my_list)

print(my_list)
