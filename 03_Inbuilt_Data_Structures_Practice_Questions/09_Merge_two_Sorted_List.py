def merge_two_sorted_lists(list1, list2):
    for num in list1:
        list2.append(num)

    list2.sort()

    return list2

list1 = [5,6,7,8,12]
list2 = [1,2,9,15]
lst = merge_two_sorted_lists(list1, list2)
print(lst)