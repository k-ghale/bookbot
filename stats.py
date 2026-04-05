
def read_books_text(text):
    words = text.split()
    return len(words)

def num_of_each_character(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars :
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


