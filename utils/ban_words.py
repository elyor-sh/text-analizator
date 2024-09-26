
ban_words = {}

def check_ban_words(text):
    for word in text.split():
        if word in ban_words:
            return True
    return False