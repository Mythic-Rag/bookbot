from stats import word_count, get_character_counts


def get_book_text(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def main():
    file_path = 'books/frankenstein.txt'
    book_text = get_book_text(file_path)

    num_words = word_count(book_text)
    print(f"{num_words} words found in the document")

    char_counts = get_character_counts(book_text)
    print(char_counts)

if __name__ == '__main__':
    main()
