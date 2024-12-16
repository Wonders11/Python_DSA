def generate_pyramid(n):
    row = []
    j = 1

    for i in range(n,0,-1):
        blank_space = ((2*n)-1-j)//2 # total no of digits are 2n-1 ans so at each step 2n-1-j//2 blank spaces
        row.append(" "*(blank_space) + "*"*(j) + " "*(blank_space))
        j = j+2

    return row

pattern = generate_pyramid(4)
print(pattern)