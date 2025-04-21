from stats import *
import sys

def get_book_text(path):
    with open (path) as f:
       file_content = f.read() 
    return file_content

def main(): 
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]

    book_content = get_book_text(book)
    #print(f"{count_words(book_content)} words found in the document")
    #print(f"{count_characters(book_content)}")
    print_report(book, book_content)


def print_report(book, book_content):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_content)} total words")
    print("--------- Character Count -------")
    chardict = count_characters(book_content) 
    for entry in dict_to_sorted_list(chardict):
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()




