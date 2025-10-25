import sys
from stats import get_no_of_words
from stats import get_character_frequency
from stats import create_sorted_list
from stats import sort_on
if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def main():
    filepath=sys.argv[1]
    book_text=get_character_frequency(filepath)
    book_text=create_sorted_list(book_text)
    no_of_words=get_no_of_words(filepath)
    return no_of_words, book_text
 

def print_book_stats():
  words, chars = main()
  print("=============================BOOKBOT=============================")
  print("Analyzing book found at",sys.argv[1],"\n")
  print(f"Found {words} total words \n")
  print("--------------Character count--------------")
  for char, count in chars:
      print(f"{char}: {count}")
  print("=============================END=============================")

print_book_stats()
