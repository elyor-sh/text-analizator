

def write_unique_words(unique_words: list[str], output_filename: str) -> None:
    with open(output_filename, 'w') as file:
        for word in unique_words:
            file.write(f"{word}\n")