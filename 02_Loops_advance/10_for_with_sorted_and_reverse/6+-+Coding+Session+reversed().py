# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

my_list = [6, 3, 5, 2, 1]

print(reversed(my_list))
print(list(reversed(my_list)))

my_tuple = (6, 3, 5, 2, 1)
print(list(reversed(my_tuple)))

my_dict = {"Z": 5, "A": 10, "C": 15, "M": 6}
print(list(reversed(my_dict)))
print(list(reversed(my_dict.values())))

for elem in reversed(my_list):
    print(elem)
