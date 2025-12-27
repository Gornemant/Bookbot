#Ch3 L4: Count words in book
def count_words(text):
    word_list = []
    number_of_words = 0
    word_list = text.split()
    number_of_words = len(word_list)
    return number_of_words
