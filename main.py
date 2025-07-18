from stats import word_count

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

frankenstein = "./books/frankenstein.txt"

text = get_book_text(frankenstein)

def main():
    print(word_count(text))

main()
