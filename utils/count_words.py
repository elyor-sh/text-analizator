from typing import Dict

def count_words(text: str) -> Dict[str, int]:
    words = text.split()
    wordsCount = {}

    for word in words:
        wordsCount[word] = wordsCount.get(word, 0) + 1
        
    return wordsCount    
