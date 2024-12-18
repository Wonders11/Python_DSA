def generate_number_pyramid(n):
    triangle = []
    for i in range(1, n + 1):
        row = " " * (n - i) + " ".join(map(str, range(1, i + 1))) + " " * (n - i)
        triangle.append(row)
    return triangle        

pattern = generate_number_pyramid(4)
print(pattern)