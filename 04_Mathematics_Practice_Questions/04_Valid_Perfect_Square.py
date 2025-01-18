def is_perfect_square(num):
    sq_root = int (num**0.5)

    if sq_root*sq_root == num:
        return True

    return False

num = 14
result = is_perfect_square(num)
print(result)