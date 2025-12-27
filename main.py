
#Ch2 L5: Refactor, count_words function moved to stats.py
from stats import count_words, count_characters

#Open and read file to return content
def get_book_text(file_path):
    file_contents = ""
    try:
        with open(file_path) as f:
            file_contents = f.read()
        return file_contents
    except Exception as e:
        print(f"Error encountered: {e}")
        return "Error opening file."

def main():
    book_content = ""
    num_words = 0
    num_characters = {}
    book_content = get_book_text("./books/frankenstein.txt")

    #Ch2 L3 print book content
    #print(book_content)

    #Ch2 L4: Count words in book and print how many were found
    #Ch2 L6: Count characters in book and print the result
    num_words = count_words(book_content)
    num_characters = count_characters(book_content)
    print(f"Found {num_words} total words")
    for char in num_characters:
        counted = num_characters[char]
        print(f"'{char}': {counted}")

main()
