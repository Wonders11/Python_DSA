def generate_rectangle(n, m):
    pattern = ['*'*m for _ in range(n)]
    return pattern


pattern = generate_rectangle(5,6)
print(pattern)