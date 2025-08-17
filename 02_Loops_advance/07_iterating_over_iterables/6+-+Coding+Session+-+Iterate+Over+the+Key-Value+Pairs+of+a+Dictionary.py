# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

chemical_elements = {
    "Hydrogen": "H",
    "Helium": "He",
    "Beryllium": "Be",
    "Boron": "B",
    "Carbon": "C",
    "Nitrogen": "N",
    "Oxygen": "O",
    "Fluorine": "F",
    "Neon": "Ne"
}

print(list(chemical_elements.items()))

for elem, symbol in chemical_elements.items():
    print(elem, symbol)

# Alternative

for pair in chemical_elements.items():
    print(pair)
    print(pair[0], pair[1])
