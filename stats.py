def get_no_of_words(filepath):
    with open(filepath, encoding="utf-8") as file:
        contents = file.read()
    words = contents.split()
    return len(words)

def get_character_frequency(filepath):
    with open(filepath, encoding="utf-8") as file:
        contents = file.read().lower()
    char_freq = {}
    for character in contents:
        if not character.isalpha():
            continue
        char_freq[character] = char_freq.get(character, 0) + 1
    return char_freq

def sort_on(item):
    return item[1]

def create_sorted_list(char_freq):
    return sorted(char_freq.items(), key=sort_on, reverse=True)
