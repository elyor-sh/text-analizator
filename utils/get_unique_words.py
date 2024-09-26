
def get_unique_words(wordsMap):

    words = []

    for word in wordsMap:
        if(wordsMap[word] == 1):
            words.append(word)
        
    return words