
def main():
    path="./books/frankenstein.txt"
    book_content = get_books_text(path);
    print(book_content)


def get_books_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content



main();
