def longest_word_length(s):
    max_length = 0  # Store the length of the longest word
    current_length = 0  # Store the length of the current word

    for char in s:
        if char != ' ':
            current_length += 1  # Increment the current word length
        else:
            if current_length > max_length:
                max_length = current_length  # Update max_length if needed
            current_length = 0  # Reset current_length for the next word

    # Update max_length for the last word (if any)
    if current_length > max_length:
        max_length = current_length

    return max_length

s = "The quick brown fox jumps over the lazy dog"
result = longest_word_length(s)
print(result)