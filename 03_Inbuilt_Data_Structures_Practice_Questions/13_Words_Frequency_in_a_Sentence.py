def count_word_frequency(sentence):
    # initializing empty dictionary
    result = {}

    # splitting the sentence into words
    words = sentence.split()

    for word in words:
        if word in result:
            result[word] += 1 # incrementing if word already exists
        else:
            result[word] = 1
    
    return result  


sentence = "the quick brown fox jumps over the lazy dog"
result = count_word_frequency(sentence)
print(result)