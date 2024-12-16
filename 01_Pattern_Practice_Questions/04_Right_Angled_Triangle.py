def generate_triangle(n):
    row= []

    for i in range(n):
        row.append("*"*(i+1))

    return row

pattern = generate_triangle(5)
print(pattern)