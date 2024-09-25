from utils.read_file import read_file
from utils.clean_text import clean_text
from utils.count_words import count_words
from utils.save_results import save_results
from utils.ban_words import check_ban_words

if __name__ == "__main__":
    try:
        text = read_file("test.txt")

        if(check_ban_words(text)):
            print("В тексте содержится запрещенное слово")
            exit(0)
        
        cleaned_text = clean_text(text)

        word_count = count_words(cleaned_text)

        save_results(word_count, "results.txt")

        print("Успешно посчитали...")

    except Exception as e:
        print(f"Произошла ошибка: {e}")