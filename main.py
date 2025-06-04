from stats import get_num_words, get_character_counts, get_sorted_dicts
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

# def print_character_counts(list_of_dicts):
#     for i in range(len(list_of_dicts)):


def make_report(num_words, list_of_dicts):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/")
    print("----------- Word Count ----------")
    print("Found %d total words" % num_words)
    print("--------- Character Count -------")
    for i in range(len(list_of_dicts)):
        print(f"{list_of_dicts[i]['char']}: {list_of_dicts[i]['num']}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    num_words = get_num_words(book)
    character_counts = get_character_counts(book)
    list_of_dicts = get_sorted_dicts(character_counts)
    make_report(num_words, list_of_dicts)

if __name__ == '__main__':
    main()