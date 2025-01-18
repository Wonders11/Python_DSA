def sum_of_even_numbers(n):
    sum = 0
    for i in range(1,n+1):
        sum += 2*i
    return sum

n=5
result = sum_of_even_numbers(n)
print(result)