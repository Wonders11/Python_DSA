def generate_floyds_triangle(n):
    triangle = []
    num = 1

    for i in range(1, n + 1):
        row = ""
        for j in range(i):
            row += str(num) + " "
            num += 1
        triangle.append(row.strip())  # Remove trailing whitespace

    return triangle

pattern = generate_floyds_triangle(5)
print(pattern)