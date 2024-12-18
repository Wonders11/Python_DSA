def generate_hollow_right_angled_triangle(n):
    row = []

    if n==1:
        return ["*"]
    
    row.append("*")

    for i in range(1,n-1): # from index=1 row to index n-2 row and so n-1 is mentioned as it is not included
        row.append("*" + " "*(i-1) + "*")

    row.append("*"*n)

    return row


pattern = generate_hollow_right_angled_triangle(7)
print(pattern)