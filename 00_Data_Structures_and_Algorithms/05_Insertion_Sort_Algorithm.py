def insertion_sort(lst):
    # Your code goes here
    size = len(lst)
    
    for current in range(1,size):
        current_card = lst[current]
        correct_position = current-1 # it will go from i-1 to 0
        
        while correct_position >= 0:
            if (lst[correct_position]< current_card):
                break
            else:
                lst[correct_position + 1] = lst[correct_position]
                correct_position -= 1
                
            lst[correct_position+1] = current_card
  
    return lst

lst = [12, 11, 13, 5, 6]
print("Sorted array is:", insertion_sort(lst))