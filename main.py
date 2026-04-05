from stats import read_books_text
from stats import num_of_each_character

def get_books_text(path):
    with open(path) as f:
        return f.read()

def main():
    path="./books/frankenstein.txt"
    book_content= get_books_text(path);
    words = read_books_text(book_content);
    characters = num_of_each_character(book_content);
    print(characters);

main();
