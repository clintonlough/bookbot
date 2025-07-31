from stats import *

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
   # print(f"{word_count} words found in the document")
    #print(char_count)

    big_dictionary = dictionary_sort(char_count)
    print(big_dictionary)
main()