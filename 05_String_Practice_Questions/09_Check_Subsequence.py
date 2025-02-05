def is_subsequence(s, t):
    
    i = 0  # Pointer for s
    j = 0  # Pointer for t

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1  # Move to the next character in t
        i += 1  # Always move to the next character in s

    return j == len(t)  # If j reached the end of t, it's a subsequence
        
s = "abcde"
t = "ace"
result = is_subsequence(s, t)
print(result)