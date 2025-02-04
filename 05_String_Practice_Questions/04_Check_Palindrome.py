def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


s = "A man a plan a canal Panama"
result = is_palindrome(s)
print(result)