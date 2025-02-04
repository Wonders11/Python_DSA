def count_consonants(s):
    s = s.lower()  
    vowels = 'aeiou' 
    count = 0

    for char in s:
        if char.isalpha() and char not in vowels: # isaslpha will check it is alphabet
            count += 1

    return count


s = "Hello, World!"
consonants_count = count_consonants(s)
print(len(s))
print("Number of consonants:", consonants_count)