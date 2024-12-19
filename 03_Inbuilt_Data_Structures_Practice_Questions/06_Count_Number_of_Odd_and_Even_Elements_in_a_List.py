def count_even_odd(lst):
    even = 0
    odd = 0

    for i in range(len(lst)):
        if lst[i]%2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return even,odd

numbers = [4,5,6,7,8,9,10,6,9]
even,odd = count_even_odd(numbers)
print(even)
print(odd)