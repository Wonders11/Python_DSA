def is_subset(lst1, lst2):
    # Your code goes here
    for elem1 in lst1:
        found = False
        for elem2 in lst2:
            if elem1 == elem2:
                found = True
                break
        if not found:
            return False
    return True

lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4, 5]
result = is_subset(lst1, lst2)
print(result)