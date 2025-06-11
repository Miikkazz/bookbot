from stats import get_num_words, get_char_count, sort_dicts
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    book = get_book_text(path_to_file)
    num_words = get_num_words(book)
    char_count = get_char_count(book)
    sorted_char_count = sort_dicts(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    print("---------- Character Count -------")
    for char in sorted_char_count:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

main()
