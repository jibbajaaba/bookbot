def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

frankenstein = "./books/frankenstein.txt"

def word_count(book):
    content = get_book_text(book)
    split_content = content.split()
    count = 0
    for word in split_content:
        if word:
            count += 1
    return f"{count} words found in the document"

def main():
    print(word_count(frankenstein))

main()
