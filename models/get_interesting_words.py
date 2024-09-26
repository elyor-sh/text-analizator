

def get_interesting_words(word_count):

    text = input('Пожалуйста введите интересные слова через пробел: ')

    if len(text) == 0:
        return {}

    words = text.split(" ")

    unique_words = set(words)

    interesting_words = {}

    for word in unique_words:
        if word in word_count:
            interesting_words[word] = word_count[word]
            print(f"{word}: {word_count[word]}\n")


    return interesting_words        