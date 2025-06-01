from sys import argv, path, exit

from stats import count_characters, count_words


def get_book_text(file_path):
    # This function reads the content of a book from a given file path and prints it.
    with open(file_path, "r", encoding="utf-8") as file:
        book_text = file.read()
        return book_text


def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    file_path = argv[1]

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(count_words(get_book_text(file_path)))
    print("---------- Character Count -------")
    print(count_characters(get_book_text(file_path)))
    print("============= END ===============")


main()
