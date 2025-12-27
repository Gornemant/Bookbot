#Ch2 L4: Count words in book
def count_words(text):
    word_list = []
    number_of_words = 0
    word_list = text.split()
    number_of_words = len(word_list)
    return number_of_words

#Ch2 L5: Count Characters
def count_characters(text):
    char_dict = {}
    #Convert to lower case
    lc_text = text.lower()
    for char in lc_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
