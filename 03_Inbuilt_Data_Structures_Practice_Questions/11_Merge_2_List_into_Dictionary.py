def merge_lists_to_dictionary(keys, values):
    new_dict = {}

    if len(keys) == len(values):
        for i in range((len(keys))):
            new_dict[keys[i]] = values[i]
        return new_dict
    
    return False

keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = merge_lists_to_dictionary(keys, values)
print(result)