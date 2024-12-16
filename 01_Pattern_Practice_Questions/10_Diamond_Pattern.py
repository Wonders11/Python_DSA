def generate_diamond(n):
    row = []

    # code for upper pyramid
    j = 1

    for i in range(n,0,-1):
        blank_space = ((2*n)-1-j)//2 # total no of digits are 2n-1 ans so at each step 2n-1-j//2 blank spaces
        row.append(" "*(blank_space) + "*"*(j) + " "*(blank_space))
        j = j+2

    # code for inverted pattern
    for i in range(n-1,0,-1): # here made change from n to n-1
        row.append(" "*(n-i) + "*"*(2*i-1) + " "*(n-i))

    return row

pattern = generate_diamond(4)
print(pattern)