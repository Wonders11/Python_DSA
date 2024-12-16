def generate_inverted_pyramid(n):
    row = []

    for i in range(n,0,-1):
        row.append(" "*(n-i) + "*"*(2*i-1) + " "*(n-i))

    return row

pattern = generate_inverted_pyramid(4)
print(pattern)