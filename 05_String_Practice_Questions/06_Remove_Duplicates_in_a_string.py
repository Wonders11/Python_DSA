def remove_duplicates(s):
    result = ''.join(dict.fromkeys(s))
    return result

s = "Hello, World!"
result = remove_duplicates(s)   
print(result)