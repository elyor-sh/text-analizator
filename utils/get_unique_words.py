from typing import Dict, List

def get_unique_words(wordsMap: Dict[str, int]) -> List[str]:

    words = []

    for word in wordsMap:
        if(wordsMap[word] == 1):
            words.append(word)
        
    return words