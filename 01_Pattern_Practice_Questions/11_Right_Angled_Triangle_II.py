def generate_right_angled_triangle(n):
    row= []
    j=1

    for i in range(n,0,-1):
        row.append(" "*(i-1) + "*"*j)
        j=j+1

    return row



pattern = generate_right_angled_triangle(4)
print(pattern)
