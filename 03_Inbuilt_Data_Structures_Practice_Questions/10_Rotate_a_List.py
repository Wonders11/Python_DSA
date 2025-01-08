def rotate_list(lst, k):
    n = len(lst)

    if n==0:
        return lst
    
    k = k%n # incase if k>n

    for i in range(k):
        last_element = lst.pop()
        lst.insert(0,last_element)

    return lst

lst = [1, 2, 3, 4, 5]
result = rotate_list(lst,k=2)
print(result)