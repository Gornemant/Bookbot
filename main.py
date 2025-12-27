
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

#Ch3 L4: Count words in book
def count_words(text):
    word_list = []
    number_of_words = 0
    word_list = text.split()
    number_of_words = len(word_list)
    return number_of_words

def main():
    book_content = ""
    num_words = 0
    book_content = get_book_text("./books/frankenstein.txt")

    #Ch3 L3 print book content
    #print(book_content)

    num_words = count_words(book_content)
    print(f"Found {num_words} total words")

main()
