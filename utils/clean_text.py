import string

helperWords = {"and", "or", "и", "либо"}

def clean_text(text: str) -> str:
    text = text.lower()

    for punct in string.punctuation:
        text = text.replace(punct, " ")

    for word in helperWords:
        text = text.replace(word, "")

    return text