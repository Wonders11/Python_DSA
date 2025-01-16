def is_palindromic_tuple(tup):
    reversed_tuple = tuple(reversed(tup))

    if tup == reversed_tuple:
        return True
    
    return False

input = (1, 2, 3, 2, 1)
result = is_palindromic_tuple(input)
print(result)