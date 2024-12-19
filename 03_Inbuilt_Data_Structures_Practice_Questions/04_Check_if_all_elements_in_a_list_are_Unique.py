def check_unique(lst):
    temp = lst
    new_list = list(set(lst))

    if new_list==temp:
        return True
    else:
        return False

numbers = [4,5,6,7,8,9,10,6,9]
result = check_unique(numbers)
print(result)