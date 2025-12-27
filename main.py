#Ch3 L2: Arguments
import sys
#Ch2 L5: Refactor, count_words function moved to stats.py
from stats import count_words, count_characters, sort_characters

#Open and read file to return content
def get_book_text(file_path):
    file_contents = ""
    try:
        with open(file_path) as f:
            file_contents = f.read()
        return file_contents
    except Exception as e:
        print(f"Error encountered: {e}")
        sys.exit("Encountered an error while trying to open the file, please verify the file path.")

def main():
    book_content = ""
    num_words = 0
    num_characters = {}
    sorted_character_list = []
    #Ch3 L2: replace hard coded path with argument
    #book_content = get_book_text("./books/frankenstein.txt")
    book_path = ""
    #Exits program if no argument was given
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_content = get_book_text(book_path)

    #Ch2 L3: print book content
    #print(book_content)

    #Ch2 L4: Count words in book and print how many were found
    #Ch2 L6: Count characters in book and print the result
    num_words = count_words(book_content)
    num_characters = count_characters(book_content)

    #Ch2 print results
    #print(f"Found {num_words} total words")
    #for char in num_characters:
    #    counted = num_characters[char]
    #    print(f"'{char}': {counted}")

    #Ch3 L1: Print a report
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}..." + "\n" + "----------- Word Count ----------")
    print(f"Found {num_words} total words" + "\n" + "--------- Character Count -------")
    sorted_character_list = sort_characters(num_characters)
    for entry in sorted_character_list:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()
