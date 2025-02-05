def is_substring(s, t):
    # Get the lengths of both strings
    len_s = len(s)
    len_t = len(t)

    # If t is longer than s, it can't be a substring
    if len_t > len_s:
        return False

    # Iterate over s to check for t
    for i in range(len_s - len_t + 1):
        match = True
        for j in range(len_t):
            if s[i + j] != t[j]:
                match = False
                break
        if match:
            return True
    
    return False

s = "hello world"
t = "world"
result = is_substring(s, t)
print(result)