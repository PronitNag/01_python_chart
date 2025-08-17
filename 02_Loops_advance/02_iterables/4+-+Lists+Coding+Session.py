# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

programming_languages = ["Python", "JavaScript", "C++"]

print(programming_languages[0])
print(programming_languages[1])
print(programming_languages[2])

print(len(programming_languages))

print(programming_languages[-1])

print(programming_languages[1:4])
print(programming_languages[1:3])

print(programming_languages[::-1])
print(programming_languages[::2])

print(programming_languages[1:4:2])

# Methods
programming_languages.append("C#")
print(programming_languages)

programming_languages.extend(["Swift", "Kotlin"])
print(programming_languages)

programming_languages.insert(0, "C#")
print(programming_languages)

programming_languages.remove("Python")
print(programming_languages)

programming_languages.sort()
print(programming_languages)

programming_languages.reverse()
print(programming_languages)

# Concatenate lists.
print([1, 2, 3] + [4, 5, 6])

print(bool(programming_languages))

nested_lists = [["a", "b", "c"], ["d", "e"]]

# Indexing nested list
print(nested_lists[0])
print(nested_lists[1])
print(nested_lists[2])
print(nested_lists[0][1])
