def is_subset(lst1, lst2):
    for ele1 in lst1:
        found = False # intial value is false which means not there in lst2
        for ele2 in lst2:
            if ele1 == ele2:
                found = True
                break
        if not found:
            return False
    return True


lst1 = [2,3,4]
lst2 = [1,2,3,4,5]

result = is_subset(lst1,lst2)
print(result)