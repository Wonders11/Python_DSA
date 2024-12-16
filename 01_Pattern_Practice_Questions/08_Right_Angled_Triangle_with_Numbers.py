def generate_number_triangle(n):
    row= []

    for i in range(1,n+1):
        row.append(f"{i}"*i)

    return row


pattern = generate_number_triangle(4)
print(pattern)