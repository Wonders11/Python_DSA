def merge_three_dictionaries(dict1, dict2, dict3):
    dict0 = dict1 | dict2 | dict3
    return dict0

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

result = merge_three_dictionaries(dict1, dict2, dict3)
print(result)