def merge_dicts_with_overlapping_keys(dicts):
    merged_dict = {}
    
    for d in dicts:
        for keys,values in d.items():
            if keys in merged_dict:
                merged_dict[keys] += values
            else:
                merged_dict[keys] = values
    
    return merged_dict

input = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
result = merge_dicts_with_overlapping_keys(input)
print(result)