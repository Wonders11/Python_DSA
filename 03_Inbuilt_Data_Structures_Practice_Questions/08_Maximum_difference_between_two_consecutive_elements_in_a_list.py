def max_consecutive_difference(lst):
    max_diff = 0
    for i in range(0,len(lst)-1):
        diff = abs(lst[i+1] - lst[i])

        if diff>max_diff:
            max_diff = diff
    
    return max_diff

lst = [5,9,3,0,7,12,17]
result = max_consecutive_difference(lst)
print(result)