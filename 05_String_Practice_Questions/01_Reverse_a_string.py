def reverse_string(s):
    s = s[::-1] # slicing syntax [start:stop:step] with step as -1 reverses the string.
    return s

s = "hello"
result = reverse_string(s)
print(result)