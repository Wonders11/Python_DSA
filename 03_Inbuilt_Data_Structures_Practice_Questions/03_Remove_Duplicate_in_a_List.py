def remove_duplicates(lst):
    duplicates = list(set(lst))
    return duplicates

numbers = [4,5,6,7,8,9,10,6,9]
result = remove_duplicates(numbers)
print(result)