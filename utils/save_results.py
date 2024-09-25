def save_results(word_count, output_filename):
    with open(output_filename, 'w') as file:
         for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
            file.write(f"{word}: {count}\n")