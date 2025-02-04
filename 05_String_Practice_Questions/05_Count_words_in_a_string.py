def count_words(s):
    words = s.split()
    return len(words)

s = "Hello, World!"
result = count_words(s)
print(result)