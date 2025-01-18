def is_prime(n):
    if n <= 1:  # Handle cases where n is less than or equal to 1
        return False
    for i in range(2, int(n**0.5) + 1):  # Optimize by checking up to the square root of n
        if n % i == 0:
            return False
    return True

n=6
result = is_prime(n)
print(result)

"""
loop condition to range(2, int(n**0.5) + 1).
If a number n has a divisor greater than its square root, it must also have a divisor smaller than its square root.
This optimization significantly improves the efficiency of the algorithm, especially for larger number
""" 
