def word_count(text):
    return len(text.split())

def unique_letter_count(text):
    word = text.lower().split()
    letter_and_count = {}
    for w in word:
        for l in w:
            if l in letter_and_count:
                letter_and_count[l] += 1
            else:
                letter_and_count[l] = 1
    return letter_and_count

# In your stats.py file
def sorted_letter_count(text):
    letter_and_count = unique_letter_count(text)
    # 1. Renamed 'sorted' to 'sorted_list' to avoid conflict
    sorted_list = []

    # Use the built-in sorted() function on the dictionary's items
    # to iterate in a sorted fashion (by character)
    for char, count in sorted(letter_and_count.items()):
        # Only add alphabetic characters to the report
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})

    # 2. Sort the list in-place first...
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    # ...then return the list itself.
    return sorted_list
