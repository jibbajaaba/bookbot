
def word_count(book):
    split_content = book.split()
    count = 0
    for word in split_content:
        if word:
            count += 1
    return f"{count} words found in the document"
