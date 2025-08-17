# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

my_list = [2, 1, 0, 8, 3]
print(sorted(my_list))

sorted_list = sorted(my_list)
print(type(sorted_list))

my_tuple = (2, 1, 0, 8, 3)
print(sorted(my_tuple))
print(sorted(my_tuple, reverse=True))

my_dict = {"Z": 5, "X": 10, "A": 8, "D": 15}
print(sorted(my_dict))
print(sorted(my_dict.values()))
print(sorted(my_dict.values(), reverse=True))

word = "Loops"
for char in sorted(word):
    print(char)

for char in sorted(word, reverse=True):
    print(char)
