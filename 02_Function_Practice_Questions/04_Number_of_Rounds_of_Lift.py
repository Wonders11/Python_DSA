def calculate_lift_rounds(n, capacity):
    round = n//capacity
    
    if n%capacity ==0:
        return round
    else:
        return round + 1

result = calculate_lift_rounds(4,5)
print(result)