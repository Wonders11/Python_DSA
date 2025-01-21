def selection_sort(lst):
    # Your code goes here
    size = len(lst)
    for i in range(0,size):
        # finding min and placing it at ith position
        for j in range(i,size):
            if lst[j]<lst[i]:
                lst[i],lst[j] = lst[j],lst[i] #swapping           
    return lst

lst = [64, 25, 12, 22, 11]
print("Sorted array is:", selection_sort(lst))
