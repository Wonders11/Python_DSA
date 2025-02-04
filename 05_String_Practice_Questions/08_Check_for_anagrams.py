def is_anagram(s, t):
    for char in s:
        if char not in t:
            return False

    return True

s = "anagram"
t = "nagaram"
result = is_anagram(s, t)
print(result)