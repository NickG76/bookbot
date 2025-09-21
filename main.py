from stats import word_count, sorted_letter_count
import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_url = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


# In your main.py file
def main():
    print("========== Bookbot ==========")
    print(f"Analyzing book found at {book_url}")
    text = get_book_text(book_url)
    words = word_count(text)
    print(f"--------- Word Count --------")
    print(f"Found {words} total words")
    print(f"------- Character Count --------")

    # 3. Iterate directly over the list returned by the function
    character_stats = sorted_letter_count(text)
    for item in character_stats:
        print(f"{item['char']}: {item['num']}")


if __name__ == '__main__':
    main()
