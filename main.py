from utils.read_file import read_file
from utils.clean_text import clean_text
from utils.count_words import count_words
from utils.save_results import save_results
from utils.ban_words import check_ban_words
from utils.get_unique_words import get_unique_words
from utils.write_unique_words import write_unique_words
from models.get_interesting_words import get_interesting_words

if __name__ == "__main__":
    try:
        text = read_file("test.txt")

        if(check_ban_words(text)):
            print("В тексте содержится запрещенное слово")
            exit(0)
        
        cleaned_text = clean_text(text)

        word_count = count_words(cleaned_text)

        unique_words = get_unique_words(word_count)

        interesting_words = get_interesting_words(word_count)

        save_results(word_count, "results.txt")
        save_results(interesting_words, "interestingWords.txt")

        write_unique_words(unique_words, "uniqueWords.txt")


        print("Успешно посчитали...")

    except Exception as e:
        print(f"Произошла ошибка: {e}")