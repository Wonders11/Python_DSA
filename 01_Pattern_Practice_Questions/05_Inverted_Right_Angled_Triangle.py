def generate_inverted_triangle(n):
    row = []

    for i in range(n,0,-1):
        row.append("*"*i)
    
    return row

pattern = generate_inverted_triangle(5)
print(pattern)