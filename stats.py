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

#Ch3 L1: Return sorted dictionary list
def sort_on(items):
    return items["num"]

def sort_characters(char_dictionary):
    new_list = []
    #Converts {"x": 0} into list {"char": "x", "num": 0} of dictionaries for sorting
    for char in char_dictionary:
        new_list.append({"char": char, "num": char_dictionary[char]})
    #Sorts list of dictionaries on "num" value in descending order
    new_list.sort(reverse=True, key=sort_on)
    return new_list
