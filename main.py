from stats import (
    get_num_words,
    get_num_chars,
    chars_dict_to_sorted_list,
)

import sys

def main():
    if len(sys.argv) < (2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_path(book_path)
    words = get_num_words(text)
    characters = get_num_chars(text)
    sorted_list = chars_dict_to_sorted_list(characters)
    print_report(book_path, words, sorted_list)


def get_book_path(book_path):
    with open(book_path) as f:
        return f.read()

def print_report(book_path, words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha() == True:
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()