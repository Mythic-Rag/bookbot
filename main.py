from stats import word_count, get_character_counts, get_sorted_character_counts, get_formatted_sorted_character_report
import sys

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def main():
# --- Check for command-line arguments ---
    # sys.argv[0] is the script name itself, so we need at least 2 entries for a file path.
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exit with a status code of 1 (indicating an error)
    
    # The second argument (index 1) is expected to be the book file path
    file_path = sys.argv[1] 

    # --- Read the book text ---
    try:
        book_text = get_book_text(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        sys.exit(1)
    
    # --- Generate and print the report ---    



    print("============ BOOKBOT ==========")
    print(f"Analyzing book found at {file_path}")

    num_words = word_count(book_text)
    print("---------- Word Count ---------")
    print(f"Found {num_words} total words")

    char_counts = get_character_counts(book_text)
    
    character_report = get_formatted_sorted_character_report(char_counts)

    print("------- Character Count -------")
    for item in character_report:
        if item["char"] != '':
            print(f"{item['char']}: {item['num']}")
    print("============= End ==============")

if __name__ == '__main__':
    main()
