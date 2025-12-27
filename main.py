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
    book_content = get_book_text("./books/frankenstein.txt")
    print(book_content)

main()
