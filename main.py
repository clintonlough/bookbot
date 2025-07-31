from stats import *

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(filepath, words, chars_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    #Loop through list and print the num for each char
    for chars in chars_sorted:
        char = chars['char']
        num = chars['num']
        print(f"{char}: {num}")

    print("============= END ===============")

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    big_dictionary = dictionary_sort(char_count)

    print_report(filepath, word_count, big_dictionary)

main()