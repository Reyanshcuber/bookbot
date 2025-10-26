import sys
from stats import get_no_of_words, get_character_frequency, create_sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    char_freq = get_character_frequency(filepath)
    sorted_chars = create_sorted_list(char_freq)
    word_count = get_no_of_words(filepath)
    return word_count, sorted_chars

def print_book_stats():
    words, chars = main()
    print("============================= BOOKBOT =============================")
    print(f"Analyzing book found at {sys.argv[1]}\n")
    print(f"Found {words} total words\n")
    print("-------------- Character count --------------")
    for char, count in chars:
        print(f"{char:<3} : {count}")
    print("============================= END =============================")

print_book_stats()
