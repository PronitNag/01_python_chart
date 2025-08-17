def binary_search(sequence, target):    
    low = 0
    high = len(sequence) - 1
    middle = (low + high) // 2

    while low <= high:
        if sequence[middle] == target:
            print("Found it!")
            break
        elif sequence[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

        middle = (low + high) // 2
    else:
        print(f"The target element {target} was not found.")

binary_search([2, 3, 4, 5, 6], 7)       
