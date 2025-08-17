# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

my_list = ["bb", "ddd", "z"]
print(sorted(my_list, key=len))

# Example
my_list = ["ba", "ddb", "c"]

def get_last_char(string):
    return string[-1]

for elem in sorted(my_list, key=get_last_char):
    print(elem)
