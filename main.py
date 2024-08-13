def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    print(book_text)

def get_book_text():
    with open(file_path) as f:
        return = f.read()


main()