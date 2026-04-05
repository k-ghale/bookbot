from stats import read_books_text
from stats import num_of_each_character
from stats import chars_dict_to_sorted_list

def get_books_text(path):
    with open(path) as f:
        return f.read()

def main():
    path="./books/frankenstein.txt"
    book_content= get_books_text(path);
    words = read_books_text(book_content);
    characters = num_of_each_character(book_content);
    sorted = chars_dict_to_sorted_list(characters)
    print_report(path, words, sorted)

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main();
