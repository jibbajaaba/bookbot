from stats import word_count, char_count, char_sort
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents


def main(book):
    if len(book) == 2:
        text = get_book_text(book[1])
        char_dict = char_count(text)

        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(word_count(text))
        print("--------- Character Count -------")
        char_sort(char_dict)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main(sys.argv)
