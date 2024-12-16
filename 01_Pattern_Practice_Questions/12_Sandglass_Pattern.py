def generate_sandglass(n):
    row = []
    j = 3 #changed this for below part of pattern

    # code for above part
    for i in range(n,0,-1):
        row.append(" "*(n-i) + "*"*(2*i-1) + " "*(n-i))

    # code for below part
    for i in range(n-1,0,-1):
        blank_space = ((2*n)-1-j)//2 # total no of digits are 2n-1 ans so at each step 2n-1-j//2 blank spaces
        row.append(" "*(blank_space) + "*"*(j) + " "*(blank_space))
        j = j+2

    return row

pattern = generate_sandglass(3)
print(pattern)