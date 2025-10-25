def get_no_of_words(filepath):
    with open(filepath) as file:
        contents=file.read()
    words=contents.split()
    no_of_words=len(words)
    return no_of_words
def get_character_frequency(filepath):
    with open (filepath) as file:
        contents=file.read()
        final_contents=contents.lower()
        dict={}
        
        for character in final_contents:
            if character.isalpha()==False:
                continue
            if character in dict:
                dict[character]+=1
            else:
                dict[character]=1
        return dict
def sort_on(dict):
    return dict[1]
def create_sorted_list(dict):
    sorted_list=sorted(dict.items(), key=sort_on, reverse=True)
    return sorted_list

        