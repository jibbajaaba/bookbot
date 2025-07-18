from stats import word_count, char_count, char_sort

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

frankenstein = "./books/frankenstein.txt"

text = get_book_text(frankenstein)
char_dict = char_count(text)

def main():
    print(word_count(text))
    print(char_count(text))
    print(char_sort(char_dict))

main()
