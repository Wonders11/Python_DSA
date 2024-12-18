def generate_hollow_inverted_right_angled_triangle(n):
    row = []

    if n==1:
        return ["*"]
    
    row.append("*"*n)

    for i in range(n-1,1,-1): # from index=1 row to index n-2 row and so n-1 is mentioned as it is not included
        row.append("*" + " "*(i-2) + "*")

    row.append("*")

    return row

pattern = generate_hollow_inverted_right_angled_triangle(4)
print(pattern)