def generate_hollow_square(n):
    square = []

    if n==1:
        square = ["*"]
        return square
    
    else:
        square.append("*"*n)

        for i in range(n-2):
            square.append("*" + " "*(n-2) + "*")

        square.append("*"*n)
    
    return square
        
pattern = generate_hollow_square(5)
print(pattern)