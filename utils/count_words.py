
def count_words(text):
    words = text.split()
    wordsCount = {}

    for word in words:
        wordsCount[word] = wordsCount.get(word, 0) + 1
        
    return wordsCount    
