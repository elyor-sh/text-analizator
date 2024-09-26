
ban_words = {}

def check_ban_words(text: str) -> bool:
    for word in text.split():
        if word in ban_words:
            return True
    return False