from stats import get_word_count, get_char_count, lst_of_sorted_dicts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    try:
        file_path = sys.argv[1]
        print(sys.argv)
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    text = get_book_text(file_path)
    word_count = get_word_count(text)
    char_counts = get_char_count(text)
    sorted_char_counts = lst_of_sorted_dicts(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")       
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for dictionary in sorted_char_counts:
        if dictionary["char"].isalpha():
            print(f"{dictionary['char']}: {dictionary['count']}")
    print("============= END ===============")

if __name__  ==  "__main__":
    main()