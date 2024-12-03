def generate_square(n):
    pattern = ['*'*n for _ in range(n)]
    return pattern


pattern = generate_square(5)
print(pattern)