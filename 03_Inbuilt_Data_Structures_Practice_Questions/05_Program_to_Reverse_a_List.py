def reverse_list(lst):
    rev_lst = []
    n = len(lst)
    for i in range(n-1,-1,-1):
        rev_lst.append(lst[i])
    return rev_lst

numbers = [4,5,6,7,8,9,10,6,9]
result = reverse_list(numbers)
print(result)