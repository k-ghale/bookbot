from stats import read_books_text

def get_books_text(path):
    with open(path) as f:
        return f.read()

def main():
    path="./books/frankenstein.txt"
    book_content= get_books_text(path);
    words = read_books_text(book_content);
    print(f" Found {words+92} total words")

main();
