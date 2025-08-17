# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

products = {
    "product1": {
        "brand": "A",
        "price": 5.40
    },
    "product2": {
        "brand": "B",
        "price": 7.35
    },
    "product3": {
        "brand": "C",
        "price": 2.24
    }
}

print("==== Welcome to our Catalog ====")

for product, data in products.items():
    print("--> Outer loop")
    print(product.capitalize())
    for category, value in data.items():
        print("> Nested loop")
        print(f"{category.capitalize()}: {value}")
    print()
