def linear_search(arr, target):
    size = len(arr)
    
    for i in range(0,size):
        if arr[i]==target:
            return i
            
    return -1

arr = [3, 7, 2, 5, 9]
target = 2

result = linear_search(arr, target)
print(result)