def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    total_word_count = word_counter(book_text)
    count_of_all_characters = count_characters(book_text)
    sorted_chars = get_sorted_list(count_of_all_characters)
    

    print(f"--- begin report of books {file_path} ---")
    print(f"{total_word_count} words found in the document")
    print ()
    for item in sorted_chars:
        print(f" The {item['char']} character was found {item['count']} times")
    print()
    print("--- end report ---")

 #  print(count_characters(book_text))
 #  print(book_text)    

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
        
def word_counter(book_text):
    word_list = book_text.split()
    return len(word_list)

def count_characters(book_text):
    lowered_string = book_text.lower()
    count = {}
    for character in lowered_string:
        if character not in count:
            count[character] = 1
        else:
            count[character] += 1
    return count

def sort_on(dict):
    return dict["count"]

def get_sorted_list(count):
    sorted_list = []
    for char, count in count.items():
        if not char.isalpha():
            continue
        sorted_list.append({"char": char, "count": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()