
def main():
    path="./books/frankenstein.txt"
    book_content= get_books_text(path);
    words = read_books_text(book_content);
    print(f" Found {words} total words")

def get_books_text(path):
    with open(path) as f:
        return f.read()

def read_books_text(text):
    words = text.split()
    return len(words)

main();
