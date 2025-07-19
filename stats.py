
def word_count(book):
    split_content = book.split()
    count = 0
    for word in split_content:
        if word:
            count += 1
    return f"Found {count} total words"


def char_count(words):
    char_dict = {}
    lower_case_text = words.lower()
    for char in lower_case_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_on(items):
    return items["num"]


def char_sort(dict):
    list_of_char = []
    for key, value in dict.items():
        if key.isalpha():
            list_of_char.append({"char": key, "num": value})
    list_of_char.sort(reverse=True, key=sort_on)
    for char in list_of_char:
        print(f"{char['char']}: {char['num']}")
