def next_greatest_letter(letters, target):
    for word in letters:
        if word > target:
            return word

    return letters[0]

letters = ['c', 'f', 'j']
target = 'k'
result = next_greatest_letter(letters, target)
print(result)