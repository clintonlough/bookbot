def count_words(contents):
    words = []
    words = contents.split()
    word_count = len(words)
    return word_count


def count_characters(contents):
    #List of characters to check for
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    character_count = {}
    contents_lower = contents.lower()

    #Loop through the book and count each character then write key pairs to dictionary
    for char in characters:
        count  = contents_lower.count(char)
        character_count[char] = count

    return character_count

def sort_on(items):
    return items["num"]

def dictionary_sort(dictionary):
    dictionary_list = []

    #Add new dict for each char num pair and add to list
    for char, num in dictionary.items():
        new_dict = {"char": char, "num": num}
        dictionary_list.append(new_dict)

    #sort the dictionary by count from greatest to least
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list