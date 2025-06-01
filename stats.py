def count_words(book_text):
    message = book_text.split()
    return f"Found {message.__len__()} total words"


def count_characters(book_text):
    message_dict = {}
    book_text = book_text.replace(" ", "").replace("\n", "").lower()
    for char in book_text:
        message_dict[char] = message_dict.get(char, 0) + 1

    sorted_dict = dict(sorted(message_dict.items(), key=lambda item: item[1], reverse=True))

    for char, count in sorted_dict.items():
        print(f"{char}: {count}")
