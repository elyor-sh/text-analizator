import string

def clean_text(text):
    text = text.lower()

    for punct in string.punctuation:
        text = text.replace(punct, " ")
    return text