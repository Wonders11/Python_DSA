def bubble_sort(lst):
    size = len(lst)
    
    for i in range(size):
        for j in range(size-1-i):
            if lst[j]>lst[j+1]:
                # swapping
                lst[j], lst[j+1] = lst[j+1], lst[j]
                
    return lst

lst = [64, 34, 25, 12, 22, 11, 90]
sorted_lst = bubble_sort(lst)
print("Sorted array is:", sorted_lst)